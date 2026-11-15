#!/usr/bin/env python3
"""Reconstruct the fixed teaching dataset. Default checks; --write replaces data.csv."""
import argparse
import csv
import io
import math
from pathlib import Path

OFFSETS_S = [
    [-0.12, 0.04, 0.11], [0.08, -0.06, 0.03], [-0.04, 0.09, -0.07],
    [0.05, -0.10, 0.08], [-0.08, 0.03, 0.10], [0.10, -0.05, 0.02],
    [-0.02, 0.07, -0.09],
]


def generated_bytes():
    buffer = io.StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["length_m", "trial", "cycles", "elapsed_s"])
    for length, offsets in zip([0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90], OFFSETS_S):
        for trial, offset in enumerate(offsets, 1):
            elapsed = 20 * 2 * math.pi * math.sqrt(length / 9.80665) + offset
            writer.writerow([f"{length:.2f}", trial, 20, f"{elapsed:.6f}"])
    return buffer.getvalue().encode("utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Explicitly regenerate data.csv.")
    args = parser.parse_args()
    target = Path(__file__).with_name("data.csv")
    expected = generated_bytes()
    if args.write:
        target.write_bytes(expected)
        print("Regenerated 21 synthetic teaching rows.")
    elif target.read_bytes() == expected:
        print("PASS: data.csv matches the documented generator byte-for-byte.")
    else:
        raise SystemExit("FAIL: data.csv differs; inspect changes before using --write.")
