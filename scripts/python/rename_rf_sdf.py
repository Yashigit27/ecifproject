import os
import shutil

# Specify the directory containing the SDF files
source_folder = '/media/user/282895b1-543c-4689-9ced-b38fcef5e554/PLProject/examp'  # Update with the actual path

# Specify the new folder where renamed files will be saved
destination_folder = os.path.join(source_folder, 'renamed_sdf_files')

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print(f"Created new folder: {destination_folder}")

# List all files in the source folder
ligand_files = os.listdir(source_folder)

# Loop through each file in the source folder
for file in ligand_files:
    # Check if the file is an SDF file
    if file.endswith('.sdf'):
        # Generate the new file name with the 'MS' suffix before the '.sdf' extension
        new_name = file.replace('.sdf', 'MS.sdf')
        
        # Get the full path of the original file and the new file path
        old_file_path = os.path.join(source_folder, file)
        new_file_path = os.path.join(destination_folder, new_name)
        
        # Rename and move the file to the new folder
        shutil.copy2(old_file_path, new_file_path)  # Use copy2 to preserve original file metadata
        print(f"Renamed and moved: {file} -> {new_name}")

print("All files renamed and moved successfully!")

