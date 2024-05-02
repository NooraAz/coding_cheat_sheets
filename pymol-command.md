changing transparency of sticks (1 is invisible)
```
set stick_transparency, 0.5, obj1
```

setting the digit numbers of distance calculations
```
set label_distance_digits, 2
```
    
show all NMR states
```
set all_states, on
```

split NMR states
```
split_states object_name
```

rotating molecule (based on origion)
```
rotate x, 45, object-name
rotate y, 45, object-name 
rotate z, 45, object-name
``` 

getting coordinates of an atom
```
iterate_state 1, <selection_name>, print x,y,z
```

Change color with hex 
```
color 0x006600, <selection-name>
```

Selection based on distance
```
# [select] [by residue] [all atoms, including HETATMs] [within 3 Å of any atom in residue 63]
# byresidue = byresi = byres = br. 
select br. all within 3 of resi 63

# [select] [name it Ala63] [by residue] [all atoms, including HETATMs] [within 3 Å of any atom in residue 63]
select Ala63, br. all within 3 of resi 63

# [select] [by residue] [all atoms, excluding HETATMs]  [within 3 Å of the CA atom in residue 63]
select br. pol. within 3 of 63/CA
```