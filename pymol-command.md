changing transparency of sticks (1 is invisible)
    
    set stick_transparency, 0.5, obj1

setting the digit numbers of distance calculations

    set label_distance_digits, 2
    
show all NMR states

    set all_states, on  

split NMR states

    split_states object_name

rotating molecule (based on origion)

    rotate x, 45, object-name
    rotate y, 45, object-name 
    rotate z, 45, object-name 

getting coordinates of an atom

    iterate_state 1, <selection_name>, print x,y,z

Change color with hex 

    color 0x006600, <selection-name>
