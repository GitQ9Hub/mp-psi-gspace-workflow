import yaml
import os

# Load schema
with open("schemas/v2.1/simulation.yaml", "r") as schema_file:
    schema = yaml.safe_load(schema_file)
    valid_types = schema["simulation_type"]["enum"]

# Function to validate a metadata file
def validate_metadata(file_path):
    with open(file_path, "r") as f:
        metadata = yaml.safe_load(f)
        sim_type = metadata.get("simulation_type")
        if sim_type not in valid_types:
            print(f"❌ {file_path}: Invalid simulation_type '{sim_type}'")
        else:
            print(f"✅ {file_path}: Simulation type '{sim_type}' is valid.")

# Scan metadata folder
metadata_folder = "metadata"
for filename in os.listdir(metadata_folder):
    if filename.endswith(".yaml"):
        validate_metadata(os.path.join(metadata_folder, filename))
