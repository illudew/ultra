#!/usr/bin/env python3
"""Fit a teaching-only synthetic pendulum dataset. Python standard library only.

Run: python3 case/pendulum/fit.py --verify
Input is resolved relative to this file, independent of the working directory.
The reported uncertainty is conditional OLS standard uncertainty, not a full budget.
"""
import argparse
import csv
import json
import math
from pathlib import Path
from statistics import mean


def analyse(path):
    groups = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            length = float(row["length_m"])
            cycles = int(row["cycles"])
            elapsed = float(row["elapsed_s"])
            if not (length > 0 and cycles > 0 and elapsed > 0):
                raise ValueError("Length, cycles and time must be positive.")
            groups.setdefault(length, []).append(elapsed / cycles)
    points = [(length, mean(periods) ** 2) for length, periods in sorted(groups.items())]
    n = len(points)
    if n < 3:
        raise ValueError("At least three distinct lengths are needed.")
    x_bar = mean(x for x, _ in points)
    y_bar = mean(y for _, y in points)
    sxx = sum((x - x_bar) ** 2 for x, _ in points)
    slope = sum((x - x_bar) * (y - y_bar) for x, y in points) / sxx
    intercept = y_bar - slope * x_bar
    residuals = [y - (slope * x + intercept) for x, y in points]
    if slope <= 0:
        raise ValueError("The fitted slope must be positive to estimate g.")
    variance = sum(r * r for r in residuals) / (n - 2)
    slope_se = math.sqrt(variance / sxx)
    gravity = 4 * math.pi ** 2 / slope
    return {
        "data_kind": "synthetic teaching data; not an experimental measurement",
        "observations": sum(len(v) for v in groups.values()),
        "length_groups": n,
        "slope_s2_per_m": slope,
        "intercept_s2": intercept,
        "g_m_per_s2": gravity,
        "conditional_standard_uncertainty_g": gravity * slope_se / slope,
        "max_abs_residual_s2": max(abs(r) for r in residuals),
        "points": [
            {"length_m": x, "mean_period_squared_s2": y, "residual_s2": r}
            for (x, y), r in zip(points, residuals)
        ],
        "assumptions": [
            "lengths treated as exact; free intercept; unweighted ordinary least squares",
            "squared-period errors are heteroscedastic; equal weighting is a teaching approximation",
            "uncertainty omits length calibration, reaction-time bias, finite-angle and apparatus effects",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true", help="Check published teaching-data invariants.")
    args = parser.parse_args()
    result = analyse(Path(__file__).with_name("data.csv"))
    if args.verify:
        assert result["observations"] == 21 and result["length_groups"] == 7
        assert abs(result["g_m_per_s2"] - 9.80665) < 0.03
        assert result["max_abs_residual_s2"] < 0.01
        assert 0 < result["conditional_standard_uncertainty_g"] < 0.03
    print(json.dumps(result, ensure_ascii=False, indent=2))
