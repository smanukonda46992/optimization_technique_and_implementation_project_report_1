import csv
import math
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
IN_CSV = ROOT / "results" / "raw_data" / "benchmark_results.csv"
OUT_DIR = ROOT / "results" / "plots"


def load_rows():
    rows = []
    with open(IN_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["size"] = int(row["size"])
            row["baseline_mean_s"] = float(row["baseline_mean_s"])
            row["optimized_mean_s"] = float(row["optimized_mean_s"])
            row["speedup"] = float(row["speedup"])
            rows.append(row)
    return rows


def plot_timings(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["distribution"]].append(row)

    fig, axes = plt.subplots(2, 3, figsize=(16, 9), constrained_layout=True)
    axes = axes.flatten()

    for i, (dist, dist_rows) in enumerate(sorted(grouped.items())):
        dist_rows = sorted(dist_rows, key=lambda r: r["size"])
        x = [r["size"] for r in dist_rows]
        baseline = [None if math.isnan(r["baseline_mean_s"]) else r["baseline_mean_s"] for r in dist_rows]
        optimized = [None if math.isnan(r["optimized_mean_s"]) else r["optimized_mean_s"] for r in dist_rows]

        ax = axes[i]
        ax.plot(x, baseline, marker="o", label="Baseline deterministic")
        ax.plot(x, optimized, marker="s", label="Optimized randomized")
        ax.set_title(dist.replace("_", " ").title())
        ax.set_xlabel("Input size")
        ax.set_ylabel("Time (seconds)")
        ax.grid(True, alpha=0.3)

    axes[-1].axis("off")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower right")

    out_path = OUT_DIR / "timings_by_distribution.png"
    fig.suptitle("Quicksort Timing: Baseline vs Optimized", fontsize=16)
    plt.savefig(out_path, dpi=200)
    plt.close(fig)


def plot_speedup(rows):
    grouped = defaultdict(list)
    for row in rows:
        grouped[row["distribution"]].append(row)

    plt.figure(figsize=(10, 6))
    for dist, dist_rows in sorted(grouped.items()):
        dist_rows = sorted(dist_rows, key=lambda r: r["size"])
        x = [r["size"] for r in dist_rows]
        y = [None if math.isnan(r["speedup"]) else r["speedup"] for r in dist_rows]
        plt.plot(x, y, marker="o", label=dist.replace("_", " ").title())

    plt.axhline(1.0, linestyle="--", color="gray", label="Parity")
    plt.title("Speedup (Baseline / Optimized)")
    plt.xlabel("Input size")
    plt.ylabel("Speedup factor")
    plt.grid(True, alpha=0.3)
    plt.legend()

    out_path = OUT_DIR / "speedup_summary.png"
    plt.savefig(out_path, dpi=200)
    plt.close()


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_rows()
    plot_timings(rows)
    plot_speedup(rows)
    print(f"Saved plots in: {OUT_DIR}")


if __name__ == "__main__":
    main()
