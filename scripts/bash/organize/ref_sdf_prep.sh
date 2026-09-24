#!/bin/bash

# Define source and destination directories
SOURCE_DIR="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/PLProject/PDB_refined_kinase"
DEST_DIR="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/PLProject/prepared_refined"

# Create destination folder if it doesn't exist
mkdir -p "$DEST_DIR"

# Loop through each protein folder inside PDB_refined_kinase
for protein_folder in "$SOURCE_DIR"/*/; do
    # Copy all .sdf files to the single destination folder
    find "$protein_folder" -maxdepth 1 -type f -iname "*.sdf" -print0 | xargs -0 cp -t "$DEST_DIR/" 2>/dev/null
done

echo "All .sdf files have been copied to $DEST_DIR!"
