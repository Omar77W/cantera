import cantera as ct
import numpy as np

gas = ct.Solution("gri30.yaml")

air = "O2:0.21,N2:0.79"
fuel_comp = "C3H8:0.3,NH3:0.7"
phi = 0.6
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
T = 300
P = 500000
gas.TP = T, P
nu = gas.viscosity/gas.density    # kinematic viscosity

# Domain width in metres
width = 0.014

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

# Define logging level
loglevel = 1

flame.solve(loglevel=loglevel, auto=True)
D_1 = nu/flame.velocity[0]   # flame thickness = kin. viscosity/flame speed



phi = 0.7
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_2 = nu/flame.velocity[0]



phi = 0.8
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_3 = nu/flame.velocity[0]



phi = 0.9
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_4 = nu/flame.velocity[0]



phi = 1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_5 = nu/flame.velocity[0]



phi = 1.1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_6 = nu/flame.velocity[0]



phi = 1.2
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_7 = nu/flame.velocity[0]



phi = 1.3
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_8 = nu/flame.velocity[0]



phi = 1.4
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_9 = nu/flame.velocity[0]



phi = 1.5
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

# Create the flame object
flame = ct.FreeFlame(gas, width=width)

# Define tolerances for the solver
flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)

flame.solve(loglevel=loglevel, auto=True)
D_10 = nu/flame.velocity[0]


print(f"Flame thickness at 0.6 is: {D_1 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 0.7 is: {D_2 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 0.8 is: {D_3 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 0.9 is: {D_4 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 1.0 is: {D_5 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 1.1 is: {D_6 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 1.2 is: {D_7 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 1.3 is: {D_8 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 1.4 is: {D_9 * 1000000:.5f} micro m/s")
print(f"Flame thickness at 1.5 is: {D_10 * 1000000:.5f} micro m/s")

print("     ")

print(D_1 * 1000000)
print(D_2 * 1000000)
print(D_3 * 1000000)
print(D_4 * 1000000)
print(D_5 * 1000000)
print(D_6 * 1000000)
print(D_7 * 1000000)
print(D_8 * 1000000)
print(D_9 * 1000000)
print(D_10 * 1000000)
