#!/bin/bash

# Use your Schrödinger installation path
SCHRODINGER=/home/user/softwares/Schrodinger

# Input directories
PROT_MAE="protein_split"
LIG_MAE="ligand_split"

# Output directories
PROT_PDB="protein_split_pdb"
LIG_SDF="ligand_split_sdf"

mkdir -p "$PROT_PDB" "$LIG_SDF"

# Convert proteins: MAE → PDB
for prot in "$PROT_MAE"/*.mae; do
    base=$(basename "$prot" .mae)
    echo "Converting protein $prot → $PROT_PDB/${base}.pdb"
    "$SCHRODINGER/utilities/structconvert" "$prot" "$PROT_PDB/${base}.pdb"
done

# Convert ligands: MAE → SDF
for lig in "$LIG_MAE"/*.mae; do
    base=$(basename "$lig" .mae)
    echo "Converting ligand $lig → $LIG_SDF/${base}.sdf"
    "$SCHRODINGER/utilities/structconvert" "$lig" "$LIG_SDF/${base}.sdf"
done

echo "✅ Conversion complete. Proteins in $PROT_PDB, Ligands in $LIG_SDF"

