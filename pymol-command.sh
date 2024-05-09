# changing transparency of sticks (1 is invisible)
set stick_transparency, 0.5, obj1

# setting the digit numbers of distance calculations
set label_distance_digits, 2
    
# show all NMR states
set all_states, on

# split NMR states
split_states object_name

# rotating molecule (based on origion)
rotate x, 45, object-name
rotate y, 45, object-name 
rotate z, 45, object-name

# getting coordinates of an atom
iterate_state 1, <selection_name>, print x,y,z

# Change color with hex 
color 0x006600, <selection-name>

# increases the number of cartoon segments
set cartoon_sampling, 10

# Selection based on distance
## [select] [by residue] [all atoms, including HETATMs] [within 3 Å of any atom in residue 63]
## byresidue = byresi = byres = br. 
select br. all within 3 of resi 63

## [select] [name it Ala63] [by residue] [all atoms, including HETATMs] [within 3 Å of any atom in residue 63]
select Ala63, br. all within 3 of resi 63

## [select] [by residue] [all atoms, excluding HETATMs]  [within 3 Å of the CA atom in residue 63]
select br. pol. within 3 of 63/CA

# load from pdb
## async=0 means "don't perform the next command until this one is not finished"
fetch <pdb-id>, async=0

# show it as blue/magenta spheres
as spheres
color lightblue, not org
color magenta, org

remove solvent

# set the view

orient all within 8 of org

# set the lights, ray tracing setttings
# to get the Goodsell-like rendering

unset specular

set ray_trace_gain, 0

set ray_trace_mode, 3

bg_color white

set ray_trace_color, black

unset depth_cue

ray