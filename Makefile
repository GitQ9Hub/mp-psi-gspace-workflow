# Project: MP × PSI × G-Space Integration Workflow

# Paths
ENV_FILE=environment.yml
MERGE_SCRIPT=scripts/merge_metadata.py
VALIDATE_SCRIPT=scripts/validate_metadata.py
NOTEBOOK=notebooks/metadata_merge.ipynb

# Targets
.PHONY: all setup merge validate notebook clean validate-all validate-metadata help

all: setup merge validate

# 🧰 Environment setup
setup:
	@echo "🔧 Creating conda environment..."
	conda env create -f $(ENV_FILE) || echo "Environment already exists."

# 📊 Metadata merging
merge:
	@echo "📊 Merging metadata from MP, PSI, and G-Space..."
	python $(MERGE_SCRIPT)

# 🔍 Validation of merged metadata
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
help:
	@echo "🛠️  Available targets:"
	@echo "  setup              - Create conda environment"
	@echo "  merge              - Merge metadata from MP, PSI, and G-Space"
	@echo "  validate           - Validate merged metadata"
	@echo "  validate-all       - Validate all *_example.yaml files"
	@echo "  validate-metadata  - Validate specific example files"
	@echo "  notebook           - Launch JupyterLab with merge notebook"
	@echo "  clean              - Remove processed data and results"

# 🔄 validate-all target
validate-all:
	@echo "🔍 Validating all *_example.yaml files..."
	@for file in $(shell find schemas/v2.1 -name '*_example.yaml'); do \
		echo "🔍 Validating $$file..."; \
		python scripts/load_simulation_yaml.py $$file || exit 1; \
	done
	@echo "✅ All example files validated successfully."

# 🔄 validate-metadata targt
validate-metadata:
	@echo "🔍 Validating atom_example.yaml..."
	@python scripts/load_simulation_yaml.py schemas/v2.1/atom_example.yaml
	@echo "🔍 Validating ml_example.yaml..."
	@python scripts/load_simulation_yaml.py schemas/v2.1/ml_example.yaml
	@echo "🔍 Validating psi_example.yaml..."
	@python scripts/load_simulation_yaml.py schemas/v2.1/psi_example.yaml
	@echo "✅ All metadata examples validated successfully."

