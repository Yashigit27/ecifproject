#!/bin/bash
# Define source and destination directories
SOURCE_DIR="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/PLProject/PDB_general_kinase"
DEST_DIR="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/PLProject/General_mol"

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Loop through each protein folder inside PDB_general_kinase
for protein_folder in "$SOURCE_DIR"/*/; do
    # Extract the protein name (folder name)
    protein_name=$(basename "$protein_folder")
    
    # Create a corresponding folder inside General_mol
    mkdir -p "$DEST_DIR/$protein_name"
    
    # Copy .mol2 files from the source folder to the corresponding folder in General_mol
    cp "$protein_folder"/*.mol2 "$DEST_DIR/$protein_name/" 2>/dev/null
    
    # Check if any .mol2 files were copied
    if ls "$DEST_DIR/$protein_name/"*.mol2 &>/dev/null; then
        echo "Copied .mol2 files for $protein_name"
    else
        echo "No .mol2 files found for $protein_name"
    fi
done

echo "Task completed!"
