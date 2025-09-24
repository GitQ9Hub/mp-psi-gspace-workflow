# 📦 Required Package
# Install jsonschema if you haven’t already:
pip install jsonschema

# Import library

import pandas as pd
import json
import jsonschema
from jsonschema import validate
from pathlib import Path

# Paths
csv_path = Path("../data_processed/merged_metadata.csv")
schema_path = Path("../metadata/schema.json")

# Load schema
with open(schema_path, "r") as f:
    schema = json.load(f)

# Load CSV
df = pd.read_csv(csv_path)

# Track validation results
errors = []

# Validate each row
for idx, row in df.iterrows():
    record = row.dropna().to_dict()  # Drop NaNs for cleaner validation
    try:
        validate(instance=record, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        errors.append({
            "row": idx,
            "error": str(e.message),
            "record": record
        })

# Report
if errors:
    print(f"❌ Validation failed for {len(errors)} rows.")
    for err in errors[:5]:  # Show first 5 errors
        print(f"Row {err['row']}: {err['error']}")
else:
    print("✅ All rows passed schema validation.")
    

    