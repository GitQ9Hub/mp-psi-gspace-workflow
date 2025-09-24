import pandas as pd
import os

# Normalization functions per source
def normalize_mp(df):
    df = df.rename(columns={"id": "material_id", "temp_K": "temperature"})
    df["source"] = "MP"
    return df

def normalize_psi(df):
    df = df.rename(columns={"sample_id": "material_id", "temperature_K": "temperature"})
    df["source"] = "PSI"
    return df

def normalize_gspace(df):
    df = df.rename(columns={"material": "material_id", "T": "temperature"})
    df["source"] = "G-Space"
    return df

# Mapping source to function
sources = {
    "mp": normalize_mp,
    "psi": normalize_psi,
    "gspace": normalize_gspace
}

os.makedirs("data_normalized", exist_ok=True)

for name, func in sources.items():
    path = f"data_raw/{name}_metadata.csv"
    if os.path.exists(path):
        df = pd.read_csv(path)
        df_norm = func(df)
        df_norm.to_csv(f"data_normalized/{name}_normalized.csv", index=False)
        print(f"✅ Normalized {name} metadata")
    else:
        print(f"⚠️ Missing file: {path}")
