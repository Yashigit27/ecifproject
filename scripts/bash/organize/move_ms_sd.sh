#!/bin/bash

# Define the source folder where the renamed ligand files are located
source_folder="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/PLProject/ms_sdf_general/renamed_sdf_files"

# Define the parent folder where protein folders are located
protein_parent_folder="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/PLProject/PDB_general_kinase"

# Loop through all .sdf files in the renamed_sdf_files folder
for ligand_file in "$source_folder"/*.sdf; do
    if [ -f "$ligand_file" ]; then
        # Extract the ligand file name without extension
        ligand_name=$(basename "$ligand_file" .sdf)
        
        # Assume the protein code is part of the ligand file name (e.g., "proteinCode_ligand.sdf")
        # Here, we split the ligand name to get the protein code (adjust as needed based on your naming convention)
        protein_code=$(echo "$ligand_name" | cut -d'_' -f1)

        # Define the protein folder path using the protein code
        protein_folder="$protein_parent_folder/$protein_code"
        
        # Check if the protein folder exists
        if [ -d "$protein_folder" ]; then
            # Copy the ligand file to the respective protein folder
            cp "$ligand_file" "$protein_folder/"
            echo "Copied $ligand_name to $protein_folder/"
        else
            echo "Protein folder $protein_folder does not exist for ligand $ligand_name."
        fi
    fi
done

echo "All relevant ligand files copied successfully!"

