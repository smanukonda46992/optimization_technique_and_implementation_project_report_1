import csv
import math
import statistics
import time
from pathlib import Path

from src.baseline_quicksort import deterministic_quicksort
from src.input_generators import (
    duplicate_heavy_array,
    nearly_sorted_array,
    random_array,
    reverse_sorted_array,
    sorted_array,
)
from src.optimized_quicksort import optimized_randomized_quicksort


ROOT = Path(__file__).resolve().parents[1]
OUT_CSV = ROOT / "results" / "raw_data" / "benchmark_results.csv"


def time_function(fn, arr):
    arr_copy = list(arr)
    start = time.perf_counter()
    fn(arr_copy)
    end = time.perf_counter()
    return end - start


def summarize(values):
    numeric = [v for v in values if v is not None and not math.isnan(v)]
    if not numeric:
        return math.nan, math.nan
    return statistics.mean(numeric), statistics.pstdev(numeric)


def run():
    sizes = [100, 500, 1000, 2000, 3000, 5000, 7500]
    trials = 5

    generators = {
        "random": random_array,
        "sorted": sorted_array,
        "reverse_sorted": reverse_sorted_array,
        "nearly_sorted": nearly_sorted_array,
        "duplicates": duplicate_heavy_array,
    }

    rows = []

    for dist_name, generator in generators.items():
        for size in sizes:
            base_times = []
            opt_times = []

            for _ in range(trials):
                data = generator(size)
                try:
                    base_times.append(time_function(deterministic_quicksort, data))
                except RecursionError:
                    base_times.append(math.nan)

                try:
                    opt_times.append(time_function(optimized_randomized_quicksort, data))
                except RecursionError:
                    opt_times.append(math.nan)

            base_mean, base_std = summarize(base_times)
            opt_mean, opt_std = summarize(opt_times)

            if math.isnan(base_mean) or math.isnan(opt_mean) or opt_mean <= 0:
                speedup = math.nan
            else:
                speedup = base_mean / opt_mean

            rows.append(
                {
                    "distribution": dist_name,
                    "size": size,
                    "baseline_mean_s": base_mean,
                    "baseline_std_s": base_std,
                    "optimized_mean_s": opt_mean,
                    "optimized_std_s": opt_std,
                    "speedup": speedup,
                }
            )

            baseline_display = "FAIL" if math.isnan(base_mean) else f"{base_mean:.6f}s"
            optimized_display = "FAIL" if math.isnan(opt_mean) else f"{opt_mean:.6f}s"
            speedup_display = "N/A" if math.isnan(speedup) else f"{speedup:.2f}x"

            print(
                f"{dist_name:14} size={size:5d} "
                f"baseline={baseline_display} optimized={optimized_display} speedup={speedup_display}"
            )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "distribution",
                "size",
                "baseline_mean_s",
                "baseline_std_s",
                "optimized_mean_s",
                "optimized_std_s",
                "speedup",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"\nSaved results to: {OUT_CSV}")


if __name__ == "__main__":
    run()
