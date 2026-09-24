#!/bin/bash

# ==== CONFIG ====
INPUT_DIR="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/pdb_complexes_train"
PROT_DIR="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/protein_split_train"
LIG_DIR="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/ligand_split_train"

mkdir -p "$PROT_DIR" "$LIG_DIR"

# ==== SPLIT LOOP ====
for file in "$INPUT_DIR"/*.pdb; do
    base=$(basename "$file" .pdb)
    echo "Processing $base ..."

    OUT_PREFIX="${base}_split"

    # Use full paths so Schrödinger writes to desired directories
    $SCHRODINGER/run split_structure.py \
        -m ligand -many_files \
        "$file" "${PROT_DIR}/${OUT_PREFIX}.mae"

    # Move ligand MAE files
    for ligfile in "${base}_split_ligand"*.mae; do
        if [[ -f "$ligfile" ]]; then
            mv "$ligfile" "$LIG_DIR/${base}_ligand.mae"
            break  # take first ligand only
        fi
    done

    echo "✅ Finished $base"
done

echo "🎯 Splitting completed!"

