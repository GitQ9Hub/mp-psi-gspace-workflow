# Project: MP × PSI × G-Space Integration Workflow

# Paths
ENV_FILE=environment.yml
MERGE_SCRIPT=scripts/merge_metadata.py
VALIDATE_SCRIPT=scripts/validate_metadata.py
NOTEBOOK=notebooks/metadata_merge.ipynb

# Targets
.PHONY: all setup merge validate notebook clean

all: setup merge validate

setup:
	@echo "🔧 Creating conda environment..."
	conda env create -f $(ENV_FILE) || echo "Environment already exists."

merge:
	@echo "📊 Merging metadata from MP, PSI, and G-Space..."
	python $(MERGE_SCRIPT)

validate:
	@echo "✅ Validating merged metadata against schema..."
	python $(VALIDATE_SCRIPT)

notebook:
	@echo "🚀 Launching JupyterLab..."
	jupyter lab $(NOTEBOOK)

clean:
	@echo "🧹 Cleaning processed data and results..."
	rm -f data_processed/*.csv
	rm -rf results/*