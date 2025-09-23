
# mp-psi-gspace-workflow

A reproducible, open-science workflow integrating computational data from the Materials Project (MP), experimental microgravity datasets from NASA PSI, and simulation outputs from the G-Space platform. This project aligns metadata across sources, validates predictions, and extracts features for machine learning—advancing interdisciplinary research in materials science and space environments.

---

## 📁 Folder Structure
├── scripts/            # Python scripts for validation and mapping
│   ├── validate_simulation.py  # Validates simulation_type in metadata
│   └── validate_metadata.py    # Validates full metadata structure (fields, types)

---

## 🧠 Project Highlights

- **Simulation Tagging**: Metadata files are tagged with `simulation_type: ATOM` or `simulation_type: ML` to distinguish physics-based vs. ML-based simulations.
- **Schema Evolution**: YAML schema in `schemas/v2.1/` defines allowed simulation types and supports future extensibility.
- **Validation Logic**: Python script reads metadata and checks conformity against schema—ensuring consistency and reproducibility.
- **Integration Strategy**: Aligns MP’s DFT predictions with PSI’s experimental outputs and G-SPACE’s hybrid simulations to enable cross-validation and feature extraction.
3. Run the simulation type validator:
   ```bash
   python scripts/validate_simulation.py
---

## 🚀 Getting Started

1. Clone the repository
2. Activate the Conda environment:
   ```bash
   conda env create -f environment.yml
   conda activate mp-psi-gspace
# 🧬 MP × PSI × G-Space Integration Workflow

This project showcases a modular, reproducible workflow for integrating simulation metadata across the Materials Project, NASA PSI, and G-Space. It supports both atomic-scale (ATOM) and machine learning (ML) simulation types, with clear schema logic and scalable validation.

---

## 🚀 Project Goals

- Align metadata standards across interdisciplinary teams
- Enable seamless onboarding for new collaborators
- Support conditional validation and UI generation
- Showcase reproducible schema evolution and modular design

---

## 📁 Key Components

```bash
schemas/v2.1/
├── simulation.yaml
├── atom.yaml
├── ml.yaml
├── load_simulation_yaml.py
├── Makefile
├── environment.yml
