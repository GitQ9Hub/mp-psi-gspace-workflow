
# mp-psi-gspace-workflow

A reproducible, open-science workflow integrating computational data from the Materials Project (MP), experimental microgravity datasets from NASA PSI, and simulation outputs from the G-Space platform. This project aligns metadata across sources, validates predictions, and extracts features for machine learning—advancing interdisciplinary research in materials science and space environments.

---

## 📁 Folder Structure

├── data_raw/           # Unprocessed metadata from MP, PSI, and G-Space
├── data_processed/     # Cleaned and merged metadata files
├── metadata/           # Schema definitions and validation logic
├── scripts/            # Python scripts for merging and validating metadata
├── notebooks/          # Jupyter notebooks for exploratory analysis
├── results/            # Output files, plots, and ML predictions
├── environment.yml     # Conda environment for reproducibility
├── Makefile            # Automation for setup, merge, validate, and launc
Add folder structure to README
