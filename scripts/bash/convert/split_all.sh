#!/bin/bash

mkdir -p proteins ligands ligands_sdf proteins_pdb

for file in pdb_complex_kinase/*.pdb; do
    base=$(basename "$file" .pdb)
    echo "Processing $base..."

    $SCHRODINGER/run split_structure.py -m ligand -many_files "$file" proteins/${base}_protein.mae
done

# Move ligand files to ligands folder
mv proteins/*_ligand.mae ligands/

# Convert ligands to SDF
for lig in ligands/*.mae; do
    base=$(basename "$lig" .mae)
    $SCHRODINGER/utilities/structconvert "$lig" ligands_sdf/${base}.sdf
done

# Convert proteins to PDB
for prot in proteins/*.mae; do
    base=$(basename "$prot" .mae)
    $SCHRODINGER/utilities/structconvert "$prot" proteins_pdb/${base}.pdb
done

