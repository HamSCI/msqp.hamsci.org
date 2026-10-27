"""Find underdense meteor echoes in WSJT-X MSK144 WAV files and fit their decay times.

For each 15 s WAV file saved by WSJT-X (named YYMMDD_HHMMSS.wav, UTC), this script:

1. Blanks impulse noise (static crashes, ignition): samples more than 5 times the
   local RMS level are zeroed. A real MSK144 echo has a near-constant envelope
   and passes through untouched. Use --blank-k 0 to turn this off.
2. Computes a signal-amplitude envelope with a short-time FFT (72 ms window by
   default, the length of one MSK144 frame), keeping only the 500-2800 Hz band.
   With --no-filter the whole audio band is used instead.
3. Finds echoes: short bursts clearly above the noise floor with a sharp rise
   and an exponential-looking decay, lasting less than 2 s.
4. Fits each echo's decay with a noise-aware exponential and reports the
   amplitude e-folding time tau, where A(t) = A0 * exp(-t / tau).
   The power e-folding time is tau / 2.
5. Plots the raw audio and the envelope, labels each echo with tau, and puts the
   matching ALL.TXT decodes in the title.

Usage (from the repository root, with radioconda's Python):
    python analysis/underdense_decay.py data
    python analysis/underdense_decay.py data --no-filter --out data/plots_nofilter

Outputs, in --out (default <data dir>/plots):
    <YYMMDD_HHMMSS>.png   one figure per WAV file
    echoes.csv            one row per fitted echo, for batch processing
"""

import argparse
import csv
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # write files only; no plot windows
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.ndimage import median_filter
from scipy.optimize import curve_fit

STAMP_RE = re.compile(r"(\d{6}_\d{6})")

# Detection settings (dB relative to the median noise floor of the file).
EDGE_DB = 2.0        # an echo starts and ends where the envelope crosses this
PEAK_DB = 4.0        # an echo's peak must reach at least this
MERGE_GAP_S = 0.10   # bursts closer together than this are one event
MAX_DURATION_S = 2.0 # underdense: shorter than this above EDGE_DB
MAX_RISE_S = 0.20    # sharp rise: onset to peak within this
FIT_TAIL_S = 0.30    # extra noise-floor time included after the echo in the fit
MIN_R2 = 0.6         # minimum goodness of fit (in dB) to accept an echo
TAU_RANGE_S = (0.005, 2.0)


@dataclass
class Decode:
    snr_db: int
    dt_s: float
    df_hz: int
    freq_mhz: str
    message: str


@dataclass
class Echo:
    t_start: float
    t_peak: float
    t_end: float
    peak_db: float
    peak_db_unfiltered: float
    tau_s: float = float("nan")
    r2: float = float("nan")
    a0: float = float("nan")
    fit_t: np.ndarray = None
    fit_amp: np.ndarray = None
    accepted: bool = False
    reason: str = ""


def read_all_txt(path):
    """Return {YYMMDD_HHMMSS: [Decode, ...]} from a WSJT-X ALL.TXT file."""
    decodes = {}
    if not path.exists():
        return decodes
    for line in path.read_text(errors="replace").splitlines():
        parts = line.split()
        # stamp, freq, Rx/Tx, mode, snr, dt, df, message...
        if len(parts) < 8 or not STAMP_RE.fullmatch(parts[0]):
            continue
        try:
            d = Decode(int(parts[4]), float(parts[5]), int(parts[6]), parts[1],
                       " ".join(parts[7:]))
        except ValueError:
            continue
        decodes.setdefault(parts[0], []).append(d)
    return decodes


def blank_impulses(x, sr, k):
    """Zero samples exceeding k times the local RMS, plus a 1 ms guard each side.

    The local RMS comes from a 24 ms running median of x^2, which impulses
    lasting a few ms barely move. Returns the blanked copy and the blank mask.
    """
    if k <= 0:
        return x, np.zeros(len(x), bool)
    # median of a chi-square(1) variable is 0.455 times its mean
    local_ms = median_filter(x ** 2, size=int(0.024 * sr), mode="nearest") / 0.455
    bad = np.abs(x) > k * np.sqrt(np.maximum(local_ms, 1e-9))
    bad = np.convolve(bad, np.ones(int(0.002 * sr)), "same") > 0
    y = x.copy()
    y[bad] = 0
    return y, bad


def envelope(x, sr, win_s, hop_s, band):
    """Short-time FFT amplitude envelope.

    Returns frame-centre times, band-limited RMS amplitude, and full-band RMS
    amplitude, both in the same units as the audio samples. Frames that touch
    WSJT-X's zero padding at the start and end of the file are flagged invalid.
    """
    n = int(round(win_s * sr))
    hop = int(round(hop_s * sr))
    w = np.hanning(n)
    starts = np.arange(0, len(x) - n + 1, hop)
    frames = np.stack([x[s:s + n] for s in starts]) * w
    spec = np.abs(np.fft.rfft(frames, axis=1)) ** 2
    freqs = np.fft.rfftfreq(n, 1 / sr)
    # Parseval for a windowed one-sided spectrum: mean square = 2*sum|X|^2 / (n*sum(w^2))
    scale = 2.0 / (n * np.sum(w ** 2))
    in_band = (freqs >= band[0]) & (freqs <= band[1])
    band_rms = np.sqrt(scale * spec[:, in_band].sum(axis=1))
    full_rms = np.sqrt(scale * spec[:, 1:].sum(axis=1))
    t = (starts + n / 2) / sr

    nonzero = np.flatnonzero(x)
    first, last = (nonzero[0], nonzero[-1]) if nonzero.size else (0, len(x))
    valid = (starts >= first) & (starts + n <= last)
    return t, band_rms, full_rms, valid


def decay_model_db(t, a0, tau, noise):
    """Envelope in dB for an exponential echo added (in power) to a noise floor."""
    return 10 * np.log10((a0 * np.exp(-t / tau)) ** 2 + noise ** 2)


def find_echoes(t, amp, amp_full, valid, hop_s):
    noise = np.median(amp[valid])
    noise_full = np.median(amp_full[valid])
    with np.errstate(divide="ignore"):  # zero padding frames give -inf, never "above"
        snr = 20 * np.log10(amp / noise)
        snr_full = 20 * np.log10(amp_full / noise_full)

    above = (snr > EDGE_DB) & valid
    edges = np.diff(np.r_[0, above.astype(int), 0])
    runs = list(zip(np.flatnonzero(edges == 1), np.flatnonzero(edges == -1) - 1))
    merged = []
    for s, e in runs:
        if merged and (t[s] - t[merged[-1][1]]) < MERGE_GAP_S:
            merged[-1][1] = e
        else:
            merged.append([s, e])

    echoes = []
    for s, e in merged:
        p = s + int(np.argmax(snr[s:e + 1]))
        if snr[p] < PEAK_DB:
            continue
        echo = Echo(t[s], t[p], t[e], snr[p], snr_full[p])
        duration = t[e] - t[s]
        if duration >= MAX_DURATION_S:
            echo.reason = f"too long ({duration:.2f} s)"
        elif t[p] - t[s] > MAX_RISE_S:
            echo.reason = f"slow rise ({t[p] - t[s]:.2f} s)"
        else:
            fit_echo(echo, t, amp, valid, p, e, noise, hop_s)
        echoes.append(echo)
    return echoes, noise


def fit_echo(echo, t, amp, valid, p, e, noise, hop_s):
    stop = min(e + int(FIT_TAIL_S / hop_s), len(t) - 1)
    sel = np.arange(p, stop + 1)
    sel = sel[valid[sel]]
    if sel.size < 4:
        echo.reason = "too few points to fit"
        return
    tt = t[sel] - t[p]
    y = 20 * np.log10(amp[sel])
    a0_guess = np.sqrt(max(amp[p] ** 2 - noise ** 2, noise ** 2))
    tau_guess = max(t[e] - t[p], 0.02) / 2
    try:
        (a0, tau), _ = curve_fit(
            lambda x, a0, tau: decay_model_db(x, a0, tau, noise),
            tt, y, p0=(a0_guess, tau_guess),
            bounds=((0, TAU_RANGE_S[0]), (np.inf, TAU_RANGE_S[1])))
    except (RuntimeError, ValueError):
        echo.reason = "fit did not converge"
        return
    resid = y - decay_model_db(tt, a0, tau, noise)
    r2 = 1 - np.sum(resid ** 2) / np.sum((y - y.mean()) ** 2)
    echo.a0, echo.tau_s, echo.r2 = a0, tau, r2
    echo.fit_t = t[p] + np.linspace(0, tt[-1], 200)
    echo.fit_amp = np.sqrt((a0 * np.exp(-(echo.fit_t - t[p]) / tau)) ** 2 + noise ** 2)
    if r2 < MIN_R2:
        echo.reason = f"not exponential (R2 {r2:.2f})"
    elif tau >= TAU_RANGE_S[1] * 0.99:
        echo.reason = "decay too slow for underdense"
    else:
        echo.accepted = True


def title_for(stamp, decodes):
    utc = datetime.strptime(stamp, "%y%m%d_%H%M%S").replace(tzinfo=timezone.utc)
    head = utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    if not decodes:
        return f"{head}   (no ALL.TXT decode at this time)"
    head += f"   {decodes[0].freq_mhz} MHz MSK144"
    lines = [head]
    for msg in dict.fromkeys(d.message for d in decodes):
        ds = [d for d in decodes if d.message == msg]
        snrs = ", ".join(f"{d.snr_db:+d}" for d in ds)
        dts = ", ".join(f"{d.dt_s:.1f}" for d in ds)
        lines.append(f"{msg}   SNR {snrs} dB   DT {dts} s   DF {ds[0].df_hz} Hz")
    return "\n".join(lines)


def plot_file(path, stamp, x, sr, t, amp, noise, echoes, decodes, n_blanked, args, out):
    accepted = [e for e in echoes if e.accepted]
    n_zoom = len(accepted)
    fig = plt.figure(figsize=(13, 7.5 if n_zoom else 5.5), constrained_layout=True)
    grid = fig.add_gridspec(2 if n_zoom else 1, max(n_zoom, 1),
                            height_ratios=[2.2, 1] if n_zoom else [1])
    ax = fig.add_subplot(grid[0, :])

    ts = np.arange(len(x)) / sr
    label_env = ("FFT envelope, full band" if args.no_filter else
                 f"FFT envelope, {args.band[0]:.0f}-{args.band[1]:.0f} Hz")
    ax.plot(ts, x, color="0.7", lw=0.3, label="raw audio samples")
    blank_note = (f", {n_blanked / sr * 1000:.0f} ms of impulses blanked"
                  if args.blank_k > 0 else ", no blanking")
    ax.plot(t, amp, color="tab:blue", lw=1.2,
            label=f"{label_env} ({args.window * 1000:.0f} ms window, RMS{blank_note})")
    ax.axhline(noise, color="tab:blue", ls=":", lw=0.8, label="envelope noise floor")

    for e in echoes:
        if e.accepted:
            ax.plot(e.fit_t, e.fit_amp, color="tab:red", lw=1.6)
            ax.annotate(f"τ = {e.tau_s * 1000:.0f} ms\n{e.peak_db:.1f} dB",
                        xy=(e.t_peak, noise * 10 ** (e.peak_db / 20)),
                        xytext=(8, 12), textcoords="offset points",
                        color="tab:red", fontsize=9, fontweight="bold")
        else:
            ax.annotate(f"rejected:\n{e.reason}",
                        xy=(e.t_peak, noise * 10 ** (e.peak_db / 20)),
                        xytext=(6, 8), textcoords="offset points",
                        color="0.35", fontsize=7)
    if accepted:
        ax.plot([], [], color="tab:red", lw=1.6, label="exponential fit (underdense echo)")

    ymax = np.max(np.abs(x)) * 1.05
    for d in decodes:
        ax.plot(d.dt_s, ymax * 0.97, marker="v", color="tab:green", ms=7)
    if decodes:
        ax.plot([], [], marker="v", ls="", color="tab:green", label="ALL.TXT decode time (DT)")

    ax.set_xlim(0, len(x) / sr)
    ax.set_ylim(-ymax, ymax)
    ax.set_xlabel("Time since start of file (s)")
    ax.set_ylabel("Amplitude (16-bit counts)")
    ax.set_title(title_for(stamp, decodes), fontsize=10, loc="left")
    ax.legend(loc="lower left", fontsize=8, ncol=2)

    for i, e in enumerate(accepted):
        z = fig.add_subplot(grid[1, i])
        lo, hi = e.t_start - 0.15, max(e.fit_t[-1], e.t_end) + 0.1
        m = (t >= lo) & (t <= hi)
        z.plot(t[m], 20 * np.log10(amp[m] / noise), color="tab:blue", lw=1)
        z.plot(e.fit_t, 20 * np.log10(e.fit_amp / noise), color="tab:red", lw=1.4)
        z.axhline(0, color="tab:blue", ls=":", lw=0.8)
        z.set_title(f"echo at {e.t_peak:.2f} s: τ = {e.tau_s * 1000:.0f} ms "
                    f"(R² {e.r2:.2f})", fontsize=9)
        z.set_xlabel("Time (s)")
        if i == 0:
            z.set_ylabel("dB above noise floor")
        z.grid(alpha=0.3)

    fig.savefig(out / f"{stamp}.png", dpi=130)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("data_dir", type=Path, help="folder with the WAV files and ALL.TXT")
    ap.add_argument("--all-txt", type=Path, help="ALL.TXT path (default: <data_dir>/ALL.TXT)")
    ap.add_argument("--out", type=Path, help="output folder (default: <data_dir>/plots)")
    ap.add_argument("--window", type=float, default=0.072, help="FFT window length in s")
    ap.add_argument("--hop", type=float, default=0.006, help="FFT window step in s")
    ap.add_argument("--band", type=float, nargs=2, default=(500.0, 2800.0),
                    metavar=("LOW", "HIGH"), help="pass band in Hz")
    ap.add_argument("--no-filter", action="store_true",
                    help="use the whole audio band instead of --band")
    ap.add_argument("--blank-k", type=float, default=5.0,
                    help="impulse blanker threshold in multiples of local RMS (0 = off)")
    args = ap.parse_args()

    out = args.out or args.data_dir / "plots"
    out.mkdir(parents=True, exist_ok=True)
    decodes = read_all_txt(args.all_txt or args.data_dir / "ALL.TXT")
    band = (0.0, np.inf) if args.no_filter else args.band

    rows = []
    for path in sorted(args.data_dir.glob("*.wav")):
        m = STAMP_RE.search(path.stem)
        if not m:
            print(f"skipping {path.name}: no YYMMDD_HHMMSS in the name")
            continue
        stamp = m.group(1)
        sr, x = wavfile.read(path)
        if x.ndim > 1:
            x = x[:, 0]
        x = x.astype(float)

        clean, blanked = blank_impulses(x, sr, args.blank_k)
        t, amp, amp_full, valid = envelope(clean, sr, args.window, args.hop, band)
        # judge padding from the original audio, not from blanked zeros
        valid &= envelope(x, sr, args.window, args.hop, band)[3]
        echoes, noise = find_echoes(t, amp, amp_full, valid, args.hop)
        plot_file(path, stamp, x, sr, t, amp, noise, echoes,
                  decodes.get(stamp, []), int(blanked.sum()), args, out)

        summary = ", ".join(
            f"{e.t_peak:.2f} s tau={e.tau_s * 1000:.0f} ms" if e.accepted
            else f"{e.t_peak:.2f} s rejected ({e.reason})" for e in echoes)
        print(f"{path.name}: {summary or 'no echoes found'}")
        for e in echoes:
            rows.append({
                "file": path.name, "utc": stamp,
                "peak_time_s": round(e.t_peak, 3),
                "duration_s": round(e.t_end - e.t_start, 3),
                "peak_snr_db": round(e.peak_db, 2),
                "peak_snr_db_unfiltered": round(e.peak_db_unfiltered, 2),
                "tau_ms": round(e.tau_s * 1000, 1),
                "fit_r2": round(e.r2, 3),
                "underdense": e.accepted, "reason": e.reason,
            })

    if rows:
        with open(out / "echoes.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
    print(f"plots and echoes.csv written to {out}")


if __name__ == "__main__":
    main()
