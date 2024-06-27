from openmm.app import *
from openmm import *
from openmm.unit import *
from sys import stdout

# Getting coordinates
# --- from PDB
pose = PDBFile('<path-to-pdb-file>')
# --- from Amber input file
amber_pose = AmberInpcrdFile('input.inpcrd')

# define forcefield 
# --- from xml
forcefield = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
# --- for amber
amber_forcefield = AmberPrmtopFile('input.prmtop', periodicBoxVectors=inpcrd.boxVectors)

# creating system 
system = forcefield.createSystem(
           pose.topology, 
           # particle mesh Ewald for the long range electrostatic interactions
           # other options: NoCutOff
           nonbondedMethod=PME, 
           # 1 nm cutoff for the direct space interactions
           nonbondedCutoff=1*nanometer, 
           # constrain the length of all bonds that involve a H atom
           constraints=HBonds
        )

system = amber_forcefield.createSystem(
            nonbondedMethod=PME, 
            nonbondedCutoff=1*nanometer, 
            constraints=HBonds
        )

# create the integrator to use for advancing the equations of motion. 
# performs Langevin dynamics (constant temperature)
integrator = LangevinMiddleIntegrator(
                # simulation temperature
                300*kelvin, 
                # friction coefficient
                1/picosecond, 
                # step size
                0.004*picoseconds
             )

# creates a Simulation object
simulation = Simulation(
                pose.topology, 
                system, 
                integrator
            )
# specifies the initial atom positions for the simulation: 
# in this case, the positions that were loaded from the PDB file.
simulation.context.setPositions(pose.positions)

# perform a local energy minimization (relaxation)
simulation.minimizeEnergy()

# adding "reporters" to the Simulation object’s list of reporters 
simulation.reporters.append(
    # writes structures to a PDB file
    PDBReporter(
        # output file
        'output.pdb', 
        # every 1000 time steps
        1000
        )
    )

simulation.reporters.append(
    # get regular status reports as a simulation runs 
    StateDataReporter(
        # write the results to the console
        stdout, 
        # every 1000 time steps
        1000, 
        # the current step index,
        step=True,
        # the potential energy of the system
        potentialEnergy=True, 
        # the temperature
        temperature=True
        )
    )

# run the simulation for 10,000 time steps
simulation.step(10000)
