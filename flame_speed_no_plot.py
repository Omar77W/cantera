import cantera as ct
import numpy as np

gas = ct.Solution("dee.yaml")

air = "O2:0.21,N2:0.79"
fuel_comp = "C3H6:0.3,NH3:0.7"
phi = 0.6
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
T = 300
P = 500000
gas.TP = T, P

# Domain width in metres
width = 0.014

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

# Define logging level
loglevel = 1

flame.solve(loglevel=loglevel, auto=True)
Su0_1 = flame.velocity[0]



phi = 0.7
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_2 = flame.velocity[0]



phi = 0.8
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_3 = flame.velocity[0]



phi = 0.9
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_4 = flame.velocity[0]



phi = 1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_5 = flame.velocity[0]



phi = 1.1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_6 = flame.velocity[0]



phi = 1.2
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_7 = flame.velocity[0]



phi = 1.3
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_8 = flame.velocity[0]



phi = 1.4
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_9 = flame.velocity[0]



phi = 1.5
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
Su0_10 = flame.velocity[0]


print(f"Flame Speed at 0.6 is: {Su0_1 * 100:.5f} cm/s")
print(f"Flame Speed at 0.7 is: {Su0_2 * 100:.5f} cm/s")
print(f"Flame Speed at 0.8 is: {Su0_3 * 100:.5f} cm/s")
print(f"Flame Speed at 0.9 is: {Su0_4 * 100:.5f} cm/s")
print(f"Flame Speed at 1.0 is: {Su0_5 * 100:.5f} cm/s")
print(f"Flame Speed at 1.1 is: {Su0_6 * 100:.5f} cm/s")
print(f"Flame Speed at 1.2 is: {Su0_7 * 100:.5f} cm/s")
print(f"Flame Speed at 1.3 is: {Su0_8 * 100:.5f} cm/s")
print(f"Flame Speed at 1.4 is: {Su0_9 * 100:.5f} cm/s")
print(f"Flame Speed at 1.5 is: {Su0_10 * 100:.5f} cm/s")

print("     ")

print(Su0_1 * 100)
print(Su0_2 * 100)
print(Su0_3 * 100)
print(Su0_4 * 100)
print(Su0_5 * 100)
print(Su0_6 * 100)
print(Su0_7 * 100)
print(Su0_8 * 100)
print(Su0_9 * 100)
print(Su0_10 * 100)
