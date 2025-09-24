# MP × PSI × G-Space Integration Workflow

A reproducible, open-science workflow integrating:
- Computational data from the **Materials Project**
- Experimental microgravity datasets from **NASA PSI**
- Simulation outputs from the **G-Space platform**

This project advances interdisciplinary research in materials science and space environments.

---

## 📁 Folder Structure

- `schemas/v2.1/` — Modular YAML schemas and metadata examples
- `scripts/` — Python scripts for merging and validation
- `notebooks/` — Jupyter notebooks for metadata exploration
- `data_raw/` and `data_processed/` — Input and output datasets
- `Makefile` — Workflow automation

---

## ⚙️ Getting Started

### Setup environment

```bash
make setup

## Demo Notebooks for nanoHUB Onboarding

This repository includes two annotated notebooks that simulate metadata normalization and integration using fictitious examples. They are designed to help new contributors understand the modular pipeline and reproducibility goals of the project.

### `psi166_demo_upload.ipynb`
- Parses a mock PSI-166 ISA-Tab metadata file
- Normalizes key fields into a modular dictionary
- Validates required fields for downstream compatibility
- Saves structured output to `normalized_psi166.yaml`

### `metadata_merge_demo.ipynb`
- Loads metadata from PSI, Materials Project (MP), and G-Space
- Merges sources with provenance-tagged keys
- Validates merged structure and exports to `merged_metadata_demo.yaml`

These notebooks illustrate how metadata from diverse sources can be harmonized using modular logic, YAML formatting, and reproducible workflows. All examples use fictitious data for demonstration purposes.
