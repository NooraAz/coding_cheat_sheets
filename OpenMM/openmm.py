from openmm.app import *
from openmm import *
from openmm.unit import *
from sys import stdout

# loading pdb
pdb = PDBFile('<path-to-pdb-file>')

# define forcefield
forcefield = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')

# creating system 
system = forcefield.createSystem(
           pdb.topology, 
           nonbondedMethod=PME,
           nonbondedCutoff=1*nanometer, 
           constraints=HBonds
        )

