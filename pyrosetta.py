# getting coordinates of an atom in pose

mypose.residue(i).xyz(mypose.residue(i).atom_index('O'))

## getting torsion angle between 4 atoms

# method 1 - error: can't find degree of freedom
atom1 = #atomID
mypose.conformation().torsion_angle(atom1,atom2,atom3,atom4)

# method 2
numeric.dihedral_degrees(xyz1,xyz2,xyz3,xyz4)
