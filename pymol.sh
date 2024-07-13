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

# Turn up the surface quality
set surface_quality, 2

# ----- Selectors -----

# Selection based on distance
## [select] [by residue] [all atoms, including HETATMs] [within 3 Å of any atom in residue 63]
## byresidue = byresi = byres = br. 
select br. all within 3 of resi 63
select byresidue all within 5 of resi 322

## [select] [name it Ala63] [by residue] [all atoms, including HETATMs] [within 3 Å of any atom in residue 63]
select Ala63, br. all within 3 of resi 63

## [select] [by residue] [all atoms, excluding HETATMs]  [within 3 Å of the CA atom in residue 63]
select br. pol. within 3 of 63/CA

# selct chain A of obj1
sele my_selection, obj1 and chain A 

# select residues 100 to 150 from obj1
sele my_selection, obj1 and resi 100-150

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

# saving settings
cd downloads
run save_settings.py
save_settings
vim /Users/eadzavar/.pymolrc-settings.py

# shadows and reflections
set reflect, <number>                          #default 0.5
set ray_shadows,0   # turn off shadows
set ray_shadows,1   # turn on shadows
# turn the setting on or off
set specular, boolean

# turn it off
set specular, off

# turn it on
set specular, on
set spec_reflect, 2
set spec_power, 1500
# set it to some value
set spec_direct_power, float

# for example turn it up
set spec_direct_power, 200
# set spec direct to real-valued number
set spec_direct, float

# turn up the spec_direct
set spec_direct, 0.75

# 
cartoon_color (color, default:-1) controls the color of the cartoon representation.
cartoon_cylindrical_helices (boolean, default: off) controls whether helices are displayed as cylinders or as a residue-based cartoon.
cartoon_debug (integer: 0-3, default: 0) is for development.
cartoon_discrete_colors (boolean, default: off) affects whether per-residue colors change at or halfway inbetween the C-alpha position.
cartoon_dumbbell_length (float, default: 1.6) is a parameter for the dumbbell cross-section.
cartoon_dumbbell_radius (float, default: 0.16) is a parameter for the dumbbell cross-section.
cartoon_dumbbell_width (float, default: 0.17) is a parameter for the dumbbell cross-section.
cartoon_fancy_helices (boolean, default: off) controls whether dumbbell or oval cross-section is used.
cartoon_fancy_sheets (boolean, default: off) controls whether or not beta-sheet strands have arrows.
cartoon_flat_cycles (integer, default: 4) is the number of cycles of “flattening” applied to beta-sheets when cartoon_flat_sheets is on.
cartoon_flat_sheets (boolean, default: on) controls whether or not beta-sheet strands are flattened.
cartoon_helix_radius (float, default: 2.25) controls the radius of the cylindrical helix representation.
cartoon_highlight_color (color, default: -1) controls the accent color.
cartoon_ladder_color (color, default: -1) controls the color of the ladder representation.
cartoon_ladder_mode (integer, default: 1) controls how the ladder is drawn.
cartoon_ladder_radius (float, default: 0.25) controls the radius of the ladder representation.
cartoon_loop_cap (integer: 0-2, default: 1) controls how loop segments are capped:
0 = not capped
1 = round cap
2 = flat cap
cartoon_loop_quality (integer, default: 6) controls how many facets are used to draw the loop cross-section.
cartoon_loop_radius (float, default: 0.2) controls the radius of loop segments.
cartoon_nucleic_acid_as_cylinders (boolean, default: on) controls whether or not PyMOL draws cartoon nucleic acids as high-quality cylinders or low-quality.
cartoon_nucleic_acid_color (color, default: -1) controls the control of nucleic acid backbone cartoons.
cartoon_nucleic_acid_mode (integer, default: 4) controls how the nucleic acid backbone is computed:
0 = use P coordinates
1 = use C1* coordinates
2 = use P coordinates and terminal 3' OH (if present)
3 = use P coordinates and terminal 5' OH (if present)
4 = use P coordinates and both terminal 3' and 5' OHs (if present)
cartoon_oval_length (float, default: 1.35) is the length of the oval cross-section.
cartoon_oval_quality (integer, default: 10) controls how many facets are used to draw the oval cross-section.
cartoon_oval_width (float, default: 0.25) is the width of the oval cross section.
cartoon_power (float, default: 2.0) affects cartoon shape.
cartoon_power_b (float, default: 0.5) affects cartoon shape.
cartoon_putty_quality (float, default: 11) controls how many facets are used.
cartoon_putty_radius (float, default: 0.4) is the default putty size.
cartoon_putty_range (float, default: 2.0) is a putty scaling parameter.
cartoon_putty_scale_max (float, default: 4.0) is a putty scaling parameter.
cartoon_putty_scale_min (float, default: 0.6) is a putty scaling parameter.
cartoon_putty_scale_power (float, default: 1.5) is a putty scaling parameter.
cartoon_putty_transform (integer, default: 0) 0 is normalized nonlinear scaling; 1 is relative nonlinear scaling; 2 is scaled nonlinear scaling; 3 is absolute nonlinear scaling; 4 is normalized linear scaling; 5 is relative linear scaling; 6 is scaled linear scaling; 7 is absolute linear scaling from the B factor; and, 8 is implied RMS scaling.
cartoon_rect_length (float, default: 1.4) is the length of the rectangle cross-section.
cartoon_rect_width (float, default: 0.4) is the width of the rectangle cross-section.
cartoon_refine (integer, default: 5) controls how much refinement is done of intermediate cartoon coordinates.
cartoon_refine_normals (integer, default: -1) controls whether or not normals are refined (-1 = automatic).
cartoon_refine_tips (integer, default: 10) controls how much the tips of beta-strands are refined (straightened).
cartoon_ring_color (color, default: -1) controls the color of ring representation.
cartoon_ring_finder (integer, default: 1) controls how rings are detected:
1 = all rings with a “C4*” or “C4” atom (e.g. nucleic acid bases)
2 = all rings with a “C4” atom (e.g. carbohydrates)
3 = all rings with a “C#” atom where # is any integer
4 = all rings
cartoon_ring_mode (integer, default: 0) controls how rings are shown:
0 = no ring (use ladders for bases, if applicable)
1 = round-edge rings
2 = square-edge rings
3 = rings with edges
4 = show ring as a sphere of approximate size
5 = show ring centers as small spheres
cartoon_ring_radius (float, default: -1) controls the radius of the sphere used to represent rings (-1.0 means compute from ring geometry).
cartoon_ring_transparency (float, default: -1.0) controls the transparency level of rings. When negative, this setting is controlled by cartoon_transparency.
cartoon_ring_width (float, default: 0.125) controls the thickness of the ring representation.
cartoon_round_helices (boolean, default: on) controls whether or not PyMOL makes helices round by forcing orientation vectors to point along the helix axes.
cartoon_sampling (integer, default: 7) controls how many facets are used to draw cartoon segments.
cartoon_side_chain_helper (boolean, default: off) controls whether or not PyMOL will hide backbone lines and sticks when the cartoon representation is visible as well as disabling smoothing for C-alpha coordinates for residues whose side chains are shown.
cartoon_smooth_cycles (integer, default: 2) controls how many smoothing cycles are applied to the overall cartoon.
cartoon_smooth_first (integer, default: 1) controls the start point for smoothing each segment.
cartoon_smooth_last (integer, default: 1) controls the stop point for smoothing of each segment.
cartoon_smooth_loops (boolean, default: off) controls whether or not loop segments are smoothed. Note that this setting modifies the apparent coordinates of the loop in order to achieve improved aesthetics.
cartoon_throw (float, default: 1.35) affects cartoon geometry.
cartoon_trace_atoms (boolean, default: off) controls whether cartoons are traced through all atoms. Note that this setting only works well for the loop and tube representations.
cartoon_transparency (float, default: 0.0) controls the transparency of cartoon representations.
cartoon_tube_cap (integer, default: 2) controls the type of cap applied to the tube, and accepts the same values as cartoon_loop_cap.
cartoon_tube_quality (integer, default: 9) controls how many facets are used in the tube cross-section.
cartoon_tube_radius (float, default: 0.5) controls the radius of tube segments.

# ---------- make a movie with scenes -----------
mset 1x60 # the length of video, by frames
# set the scene that you like and save it
scene 001, store
# set the next scene and save it
scene 002, store
# store scene 001 at frame 1
mview store,  1, scene=001
# store scene 002 at frame 30
mview store, 30, scene=002 
# play 
mplay


# ---------- make a movie with view (camera movement) -----------
mset 1x60 # the length of video, by frames
# set the view point that you like and
# store the view point at frame 1
mview store,  1
# next one
mview store, 30
# play 
mplay

