# importing pose
## from file
pyrosetta.rosetta.core.import_pose.pose_from_file(file_path)


# getting coordinates of an atom in pose
mypose.residue(i).xyz(mypose.residue(i).atom_index('O'))

# number of atoms in a residue
myopse.residue(i).natoms() 

# atom element for atom index 'a' in residue 'i'
mypose.residue(i).atom_type(a).element()

## getting torsion angle between 4 atoms
# method 1 - error: can't find degree of freedom
atom1 = #atomID
mypose.conformation().torsion_angle(atom1,atom2,atom3,atom4)
# method 2
numeric.dihedral_degrees(xyz1,xyz2,xyz3,xyz4)

# getting bond length between two atoms
# a and b are atomIDs
# atomID(i,j): i is atom index and j is resuidue index
mypose.conformation().bond_length(a,b)
