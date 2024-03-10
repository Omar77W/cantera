import numpy as np
import cantera as ct

# Define your chemical mechanism and initial conditions
gas = ct.Solution("gri30.yaml")  # Replace 'your_mechanism.cti' with your mechanism file

air = "O2:0.21,N2:0.79"
T_u = 300
fuel_comp = ["C3H8:0.3,NH3:0.7", "C3H8:0.5,NH3:0.5", "C3H8:1,NH3:0"]
P = range(100000, 1450000, 50000)
phi = 1.2
Pe = 2000
R_cr = {}

for f in fuel_comp:
    R_cr_tmp = []
    for pr in P:
        gas.set_equivalence_ratio(phi=phi, fuel=f, oxidizer=air)
        gas.TP = T_u, pr
        nu = gas.viscosity/gas.density
            
        # Domain width in metres
        width = 0.014

        # Create the flame object
        flame = ct.FreeFlame(gas, width = width)

        # Define tolerances for the solver
        flame.set_refine_criteria(ratio=3, slope=0.1, curve=0.1)
        
        # Define logging level
        loglevel = 1

        flame.solve(loglevel=loglevel, auto=True)
        Su0_1 = flame.velocity[0]
        
        thickness = nu / Su0_1
        R_cr_tmp.append(1000 * thickness * Pe)  # Radius in mm
    R_cr[f] = R_cr_tmp
        
for j in R_cr.keys():
    print(j)
    for i in R_cr[j]:
        print(i)
    print()