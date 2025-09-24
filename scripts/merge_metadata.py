import pandas as pd
import os

# Define input files
input_files = [
    "data_normalized/mp_normalized.csv",
    "data_normalized/psi_normalized.csv",
    "data_normalized/gspace_normalized.csv"
]

dfs = []

for path in input_files:
    if os.path.exists(path):
        print(f"✅ Loading {path}")
        dfs.append(pd.read_csv(path))
    else:
        print(f"⚠️ File not found: {path}")

# Merge and save
if dfs:
    merged = pd.concat(dfs, ignore_index=True)
    os.makedirs("data_processed", exist_ok=True)
    merged.to_csv("data_processed/merged_metadata.csv", index=False)
    print("✅ Merged metadata saved to data_processed/merged_metadata.csv")
else:
    print("❌ No input files found. Merge aborted.")
