import pandas as pd
import os
from pocket_extraction import extract_ligand_and_pocket

# Load your PDB-ligand map
df = pd.read_csv("pdb_lig.csv")  # or .tsv with sep='\t'

input_dir = "/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/pdb_complex_kinase"
lig_out_dir = "/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/lig_extract"
pocket_out_dir = "/media/user/282895b1-543c-4689-9ced-b38fcef5e554/YASHI_ECIF/pocket_extract"

os.makedirs(lig_out_dir, exist_ok=True)
os.makedirs(pocket_out_dir, exist_ok=True)

for index, row in df.iterrows():
    pdb_id = row["PDB ID"]
    ligand = row["Ligand ID"]

    pdb_path = os.path.join(input_dir, f"{pdb_id}.pdb")
    out_lig = os.path.join(lig_out_dir, f"{pdb_id}_{ligand}.pdb")
    out_pocket = os.path.join(pocket_out_dir, f"{pdb_id}_pocket.pdb")

    try:
        extract_ligand_and_pocket(
            pdb_file=pdb_path,
            output_ligand=out_lig,
            output_pocket=out_pocket,
            ligand_names=[ligand],
            multi=False,
            radius=12.0,
            quiet=True
        )
        print(f"[✓] Extracted: {pdb_id}")
    except Exception as e:
        print(f"[!] Failed: {pdb_id} -> {e}")
