#!/bin/bash

# Base directory where pdb_ids.txt is stored
BASE_DIR="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/PDB_general_kinase"
OUTPUT_DIR="$BASE_DIR/pdb_complexes_train"
ID_FILE="$BASE_DIR/pdb_ids.txt"

# Create output directory if it doesn’t exist
mkdir -p "$OUTPUT_DIR"

# Loop through each PDB ID in the text file and download
while read -r pdb_id; do
    # Skip empty lines
    [ -z "$pdb_id" ] && continue

    echo "Downloading $pdb_id ..."
    
    # Download the PDB file from RCSB
    wget -q "https://files.rcsb.org/download/${pdb_id}.pdb" -O "$OUTPUT_DIR/${pdb_id}.pdb"
    
    # Check if file downloaded successfully
    if [ -s "$OUTPUT_DIR/${pdb_id}.pdb" ]; then
        echo "✅ Saved: $OUTPUT_DIR/${pdb_id}.pdb"
    else
        echo "❌ Failed: $pdb_id"
        rm -f "$OUTPUT_DIR/${pdb_id}.pdb"
    fi
done < "$ID_FILE"

echo "✅ All downloads completed. Saved to: $OUTPUT_DIR"

