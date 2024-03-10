import numpy as np
import cantera as ct

# Define your chemical mechanism and initial conditions
gas = ct.Solution("gri30.yaml")  # Replace 'your_mechanism.cti' with your mechanism file

air = "O2:0.21,N2:0.79"
T_u = 300
fuel_comp = ["C3H8:0.3,NH3:0.7", "C3H8:0.5,NH3:0.5", "C3H8:1,NH3:0"]
P = range(100000, 1450000, 50000)
phi = [1.0, 1.2]
l_f = {}

for ph in phi:
    for f in fuel_comp:
        th = []
        for pr in P:
            gas.set_equivalence_ratio(phi=ph, fuel=f, oxidizer=air)
            gas.TP = T_u, pr
            nu = gas.viscosity/gas.density
            
            # Domain width in metres
            width = 0.014

            # Create the flame object
            flame = ct.FreeFlame(gas, width = width)

            # Define tolerances for the solver
            flame.set_refine_criteria(ratio=2, slope=0.1, curve=0.1)
        
            # Define logging level
            loglevel = 1

            flame.solve(loglevel=loglevel, auto=True)
            Su0_1 = flame.velocity[0]
        
            thickness = nu / Su0_1
            th.append(1000000 * thickness)  # Thickness in mm
        l_f[(str(ph)+" "+f)] = th
        
for j in l_f.keys():
    print(j)
    for i in l_f[j]:
        print(i)
    print()