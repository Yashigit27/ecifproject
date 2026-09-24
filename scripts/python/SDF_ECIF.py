import numpy as np
import pandas as pd
from itertools import product
from rdkit import Chem
from scipy.spatial.distance import cdist

class ECIFElements:
    def __init__(self, atom_keys_file="PDB_Atom_Keys.csv"):
        self.Atom_Keys = pd.read_csv(atom_keys_file)
        
        self.ECIF_ProteinAtoms = [
    'C;4;1;3;0;0', 'C;4;2;1;1;1', 'C;4;2;2;0;0', 'C;4;2;2;0;1',
    'C;4;3;0;0;0', 'C;4;3;0;1;1', 'C;4;3;1;0;0', 'C;4;3;1;0;1',
    'C;5;3;0;0;0', 'C;6;3;0;0;0', 'N;3;1;2;0;0', 'N;3;2;0;1;1',
    'N;3;2;1;0;0', 'N;3;2;1;1;1', 'N;3;3;0;0;1', 'N;4;1;2;0;0',
    'N;4;1;3;0;0', 'N;4;2;1;0;0', 'O;2;1;0;0;0', 'O;2;1;1;0;0',
    'S;2;1;1;0;0', 'S;2;2;0;0;0']
        self.ECIF_LigandAtoms = [
    'Br;1;1;0;0;0','C;3;3;0;1;1', 'C;4;1;1;0;0', 'C;4;1;2;0;0',
    'C;4;1;3;0;0', 'C;4;2;0;0;0', 'C;4;2;1;0;0', 'C;4;2;1;0;1',
    'C;4;2;1;1;1', 'C;4;2;2;0;0', 'C;4;2;2;0;1', 'C;4;3;0;0;0',
    'C;4;3;0;0;1', 'C;4;3;0;1;1', 'C;4;3;1;0;0', 'C;4;3;1;0;1',
    'C;4;4;0;0;0', 'C;4;4;0;0;1', 'C;5;3;0;0;0', 'C;5;3;0;1;1',
    'C;6;3;0;0;0', 'Cl;1;1;0;0;0', 'F;1;1;0;0;0', 'I;1;1;0;0;0',
    'N;3;1;0;0;0', 'N;3;1;1;0;0', 'N;3;1;2;0;0', 'N;3;2;0;0;0',
    'N;3;2;0;0;1', 'N;3;2;0;1;1', 'N;3;2;1;0;0', 'N;3;2;1;0;1',
    'N;3;2;1;1;1', 'N;3;3;0;0;0', 'N;3;3;0;0;1', 'N;3;3;0;1;1',
    'N;4;1;2;0;0', 'N;4;1;3;0;0', 'N;4;2;1;0;0', 'N;4;2;2;0;0',
    'N;4;2;2;0;1', 'N;4;3;0;0;0', 'N;4;3;0;0;1', 'N;4;3;1;0;0',
    'N;4;3;1;0;1', 'N;4;4;0;0;0', 'N;4;4;0;0;1', 'N;5;2;0;0;0',
    'N;5;3;0;0;0', 'N;5;3;0;1;1', 'O;2;1;0;0;0', 'O;2;1;1;0;0',
    'O;2;2;0;0;0', 'O;2;2;0;0;1', 'O;2;2;0;1;1', 'P;5;4;0;0;0',
    'P;6;4;0;0;0', 'P;6;4;0;0;1', 'P;7;4;0;0;0', 'S;2;1;0;0;0',
    'S;2;1;1;0;0', 'S;2;2;0;0;0', 'S;2;2;0;0;1', 'S;2;2;0;1;1',
    'S;3;3;0;0;0', 'S;3;3;0;0;1', 'S;4;3;0;0;0', 'S;6;4;0;0;0',
    'S;6;4;0;0;1', 'S;7;4;0;0;0'
]
        self.PossibleECIF = [i[0] + "-" + i[1] for i in product(self.ECIF_ProteinAtoms, self.ECIF_LigandAtoms)]
        
        self.ELEMENTS_ProteinAtoms = ["C", "N", "O", "S"]
        self.ELEMENTS_LigandAtoms = ["Br", "C", "Cl", "F", "I", "N", "O", "P", "S"]
        self.PossibleELEMENTS = [i[0] + "-" + i[1] for i in product(self.ELEMENTS_ProteinAtoms, self.ELEMENTS_LigandAtoms)]

    def GetAtomType(self, atom):
        return ";".join([atom.GetSymbol(), str(atom.GetExplicitValence()), str(len([x for x in atom.GetNeighbors() if x.GetSymbol() != "H"])), str(len([x for x in atom.GetNeighbors() if x.GetSymbol() == "H"])), str(int(atom.GetIsAromatic())), str(int(atom.IsInRing()))])
    
    def LoadSDFasDF(self, sdf_file):
        mol = Chem.MolFromMolFile(sdf_file, sanitize=False)
        mol.UpdatePropertyCache(strict=False)
        ECIF_atoms = []
        
        for atom in mol.GetAtoms():
            if atom.GetSymbol() != "H":
                pos = mol.GetConformer().GetAtomPosition(atom.GetIdx())
                ECIF_atoms.append([atom.GetIdx(), self.GetAtomType(atom), pos.x, pos.y, pos.z])
        
        df = pd.DataFrame(ECIF_atoms, columns=["ATOM_INDEX", "ECIF_ATOM_TYPE", "X", "Y", "Z"])
        return df
    
    def LoadPDBasDF(self, pdb_file):
        ECIF_atoms = []
        with open(pdb_file) as f:
            for line in f:
                if line.startswith("ATOM"):
                    ECIF_atoms.append([int(line[6:11]), line[17:20] + "-" + line[12:16].strip(), float(line[30:38]), float(line[38:46]), float(line[46:54])])
        df = pd.DataFrame(ECIF_atoms, columns=["ATOM_INDEX", "PDB_ATOM", "X", "Y", "Z"])
        df = df.merge(self.Atom_Keys, on="PDB_ATOM")[["ATOM_INDEX", "ECIF_ATOM_TYPE", "X", "Y", "Z"]]
        return df
    
    def GetPLPairs(self, pdb_protein, sdf_ligand, distance_cutoff=6.0):
        Target = self.LoadPDBasDF(pdb_protein)
        Ligand = self.LoadSDFasDF(sdf_ligand)
        
        for axis in ["X", "Y", "Z"]:
            Target = Target[(Target[axis] < Ligand[axis].max() + distance_cutoff) & (Target[axis] >           Ligand[axis].min() - distance_cutoff)]
        
        Pairs = [t + "-" + l for t, l in product(Target["ECIF_ATOM_TYPE"], Ligand["ECIF_ATOM_TYPE"])]
        Distances = cdist(Target[["X", "Y", "Z"]], Ligand[["X", "Y", "Z"]], metric="euclidean").flatten()
        df = pd.DataFrame({"ECIF_PAIR": Pairs, "DISTANCE": Distances})
        df = df[df["DISTANCE"] <= distance_cutoff]
        df["ELEMENTS_PAIR"] = df["ECIF_PAIR"].apply(lambda x: x.split("-")[0].split(";")[0] + "-" + x.split("-")  [1].split(";")[0])
        return df
    
    def GetECIF(self, pdb_protein, sdf_ligand, distance_cutoff=6.0):
        pairs = self.GetPLPairs(pdb_protein, sdf_ligand, distance_cutoff)
        return [pairs["ECIF_PAIR"].tolist().count(x) for x in self.PossibleECIF]
    
    def GetELEMENTS(self, pdb_protein, sdf_ligand, distance_cutoff=6.0):
        pairs = self.GetPLPairs(pdb_protein, sdf_ligand, distance_cutoff)
        return [pairs["ELEMENTS_PAIR"].tolist().count(x) for x in self.PossibleELEMENTS]
