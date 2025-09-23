
# mp-psi-gspace-workflow

A reproducible, open-science workflow integrating computational data from the Materials Project (MP), experimental microgravity datasets from NASA PSI, and simulation outputs from the G-Space platform. This project aligns metadata across sources, validates predictions, and extracts features for machine learning—advancing interdisciplinary research in materials science and space environments.

---

## 📁 Folder Structure

---

## 🧠 Project Highlights

- **Simulation Tagging**: Metadata files are tagged with `simulation_type: ATOM` or `simulation_type: ML` to distinguish physics-based vs. ML-based simulations.
- **Schema Evolution**: YAML schema in `schemas/v2.1/` defines allowed simulation types and supports future extensibility.
- **Validation Logic**: Python script reads metadata and checks conformity against schema—ensuring consistency and reproducibility.
- **Integration Strategy**: Aligns MP’s DFT predictions with PSI’s experimental outputs and G-SPACE’s hybrid simulations to enable cross-validation and feature extraction.

---

## 🚀 Getting Started

1. Clone the repository
2. Activate the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate mp-psi-gspace
