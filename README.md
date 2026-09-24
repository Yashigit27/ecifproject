# Protein kinase binding affinity prediction using ECIF and RDKit descriptors

This repository contains an organized pipeline for predicting protein–ligand binding affinity on **kinase** complexes. It combines **Extended Connectivity Interaction Features (ECIF)** with **RDKit** ligand descriptors and classical regression models (DT, SVR, RF, GBR, XGBoost).

Training data are curated from **PDBbind v2020**; external evaluation uses **5,265** non-overlapped kinase complexes from RCSB PDB.

---

## Repository layout

```text
ecif_github/
├── scripts/
│   ├── notebooks/          # Main pipeline notebooks (01 → 03)
│   ├── python/             # ECIF helpers, ligand/protein utilities
│   └── bash/               # Download, convert, organize workflows
├── data/
│   ├── raw/                # ID lists, activity labels, atom-type keys
│   ├── interim/            # Mid-pipeline tables (cleaning, RDKit)
│   ├── features/           # Final ECIF / merged matrices (train + external)
│   └── sample_structures/  # Example complexes (not the full 2337 / 5265 sets)
├── models/
│   ├── ecif/               # Saved ECIF-only models
│   └── merged/             # Saved ECIF+RDKit models
├── results/
│   ├── metrics/            # Summary MSE / RMSE / R² / PCC
│   ├── predictions/        # External & consensus top-20 tables
│   ├── figures/            # Pred vs actual plots
│   └── splits/             # Train/validation split pickles
└── docs/                   # Graphical abstract and notes
```

Full structure folders (**2,337** training / **5,265** external) are large and are **not** shipped here—only representative samples under `data/sample_structures/`. Feature matrices for the full cohorts are under `data/features/`.

---

## Project overview

- Curate kinase protein–ligand complexes from PDBbind v2020 (training) and RCSB PDB (external).
- Preprocess structures (split, convert, RDKit ligand standardization).
- Compute ECIF interaction features and RDKit ligand descriptors; build merged matrices.
- Hyperparameter-tune and train regressors on ECIF-only and ECIF+RDKit inputs.
- Evaluate with **MSE**, **RMSE**, **R²**, and **Pearson correlation (PCC)**.
- Predict pIC on **5,265** non-overlapped external complexes; report consensus top-20.

---

## Methodology (short)

### 1. Data collection & preprocessing

- PDBbind 2020 general set → kinase filter → **2,494** complexes at download.
- After RDKit standardization (**2,401**) and ECIF generation → **2,337** training complexes.
- External RCSB kinase download → after descriptors and PDB-ID non-overlap → **5,265** complexes.
- Labels: `data/raw/labels/training_activity.csv` (`Complex_ID`, `pIC`).
- Atom typing keys: `data/raw/reference/PDB_Atom_Keys.csv`.

### 2. Descriptor calculation

**Notebook:** `scripts/notebooks/01_descriptor_generation.ipynb`

- RDKit ligand standardization; ECIF pair counts (cutoff used in study: **6.0 Å**).
- RDKit descriptors merged with ECIF for the combined feature set.
- Outputs land in `data/features/train/` and `data/features/external/`.

### 3. Model training & evaluation

**Notebook:** `scripts/notebooks/02_model_development.ipynb`

- Models: Decision Tree, SVR, Random Forest, Gradient Boosting, XGBoost.
- Trained on ECIF-only and merged ECIF+RDKit features.
- Saved artifacts: `models/ecif/`, `models/merged/`.
- Metrics: `results/metrics/model_metrics.csv`.

### 4. External prediction

**Notebook:** `scripts/notebooks/03_external_prediction.ipynb`

- Blind / external pIC predictions for the non-overlapped set.
- Tables and top-20 consensus: `results/predictions/`.

---

## Quick start

```bash
conda install -c conda-forge rdkit scikit-learn pandas numpy matplotlib xgboost jupyter
# or: pip install -r requirements.txt
```

Open notebooks in order:

1. `scripts/notebooks/01_descriptor_generation.ipynb`
2. `scripts/notebooks/02_model_development.ipynb`
3. `scripts/notebooks/03_external_prediction.ipynb`

Update any absolute paths inside notebooks to point at this repo’s `data/` folders (e.g. `data/raw/reference/PDB_Atom_Keys.csv`).

Bash helpers for download / Maestro convert / folder organize live under `scripts/bash/` (Schrödinger Maestro optional for full structure prep).

---

## Key result files

| File | Description |
|------|-------------|
| `results/metrics/model_metrics.csv` | Validation metrics (ECIF vs merged) |
| `results/predictions/ECIF+RDKIT_4models.csv` | Multi-model external predictions |
| `results/predictions/*top20*` | Consensus high-confidence hits |
| `results/figures/` | Pred vs actual plots |

---

## Citation / reference

ECIF method: Sánchez-Cruz et al. (extended connectivity interaction features). Kinase affinity modeling as described in the associated manuscript.
