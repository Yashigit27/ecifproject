import os
from glob import glob

input_dir = "/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/final_pdb"
output_dir = "/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/protein_only"

pdb_files = glob(os.path.join(input_dir, "*.pdb"))

for pdb_path in pdb_files:
    pdb_id = os.path.basename(pdb_path).split(".")[0]
    
    # Clear previous structures
    cmd.reinitialize()
    
    # Load PDB
    cmd.load(pdb_path, "complex")
    
    # Select only protein part
    cmd.select("protein_only", "polymer.protein")  # or just "protein"
    
    # Save protein part
    out_path = os.path.join(output_dir, f"{pdb_id}_protein.pdb")
    cmd.save(out_path, "protein_only")
    
    print(f"Saved protein structure to: {out_path}")
