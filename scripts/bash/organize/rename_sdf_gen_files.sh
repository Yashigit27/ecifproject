#!/bin/bash

# Specify the source folder containing the SDF files
source_folder="/media/user/282895b1-543c-4689-9ced-b38fcef5e554/PLProject/ms_sdf_general"

# Specify the destination folder where renamed files will be saved
destination_folder="$source_folder/renamed_sdf_files"

# Check if the destination folder exists; if not, create it
if [ ! -d "$destination_folder" ]; then
    mkdir "$destination_folder"
    echo "Created new folder: $destination_folder"
fi

# Loop through all .sdf files in the source folder
for file in "$source_folder"/*.sdf; do
    # Check if the file exists
    if [ -f "$file" ]; then
        # Extract the file name without extension
        filename=$(basename "$file" .sdf)
        
        # Create the new file name by appending 'MS' before the extension
        new_name="${filename}MS.sdf"
        
        # Move the renamed file to the destination folder
        mv "$file" "$destination_folder/$new_name"
        echo "Renamed and moved: $file -> $destination_folder/$new_name"
    fi
done

echo "All files renamed and moved successfully!"

