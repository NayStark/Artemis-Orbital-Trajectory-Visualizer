import pandas as pd
import numpy as np

COLUMNS = ["jd", "calendar", "x", "y", "z", "vx", "vy", "vz"]

def load_trajectory(path):
    rows = []

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            # skip header lines
            if not line:
                continue
            if line.startswith("JDTDB") or line.startswith("#"):
                continue
            if "Calendar" in line:
                continue

            parts = [p.strip() for p in line.split(",")]

            if len(parts) < 7:
                continue

            try:
                jd = float(parts[0])

                # positions + velocity
                x = float(parts[2])
                y = float(parts[3])
                z = float(parts[4])

                vx = float(parts[5])
                vy = float(parts[6])
                vz = float(parts[7])

                rows.append([jd, parts[1], x, y, z, vx, vy, vz])

            except:
                continue

    if len(rows) == 0:
        raise ValueError("No valid rows parsed. Check CSV format.")

    return pd.DataFrame(rows, columns=COLUMNS)