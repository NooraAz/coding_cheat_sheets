import itertools as it

# different iterations

# product: AA,AB,AC,BA,BB,BC,CA,CB,CC
it.product('ABC',repeat=2) 
           
# permutations: AB,AC,BA,BC,CA,CB
it.permutations('ABC',2)

# combinations: AB,AC,BC
it.combinations('ABC',2)

# combinations_with_replacement: AA,AB,AC,BB,BC,CC
it.combinations_with_replacement('ABC',2)
