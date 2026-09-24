#!/bin/bash

SCHRODINGER=/home/user/softwares/Schrodinger

# Create output directories
mkdir -p ligands_sdf_train proteins_pdb_train

# Convert ligand MAE → SDF
for lig in ligand_train/*.mae; do
    base=$(basename "$lig" .mae)
    echo "Converting ligand $lig → ligands_sdf_train/${base}.sdf"
    $SCHRODINGER/utilities/structconvert "$lig" ligands_sdf_train/${base}.sdf
done

# Convert protein MAE → PDB
for prot in protein_train/*.mae; do
    base=$(basename "$prot" .mae)
    echo "Converting protein $prot → proteins_pdb_train/${base}.pdb"
    $SCHRODINGER/utilities/structconvert "$prot" proteins_pdb_train/${base}.pdb
done

echo "Conversion complete."

