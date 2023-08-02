import py3Dmol

# from rcsb
view = py3Dmol.view(query='pdb:1ubq')

# cartoon
view.setStyle({'cartoon':{'color':'spectrum'}})

view
