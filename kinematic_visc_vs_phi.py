import cantera as ct
import numpy as np

gas = ct.Solution("burke_plus_okafor.yaml")

air = "O2:0.21,N2:0.79"
fuel_comp = "C3H6:0.3,NH3:0.7"
phi = 0.6
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
T = 300
P = 500000
gas.TP = T, P
nu = gas.viscosity/gas.density    # kinematic viscosity

D_1 = nu



phi = 0.7
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_2 = nu



phi = 0.8
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_3 = nu



phi = 0.9
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_4 = nu



phi = 1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_5 = nu



phi = 1.1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_6 = nu



phi = 1.2
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_7 = nu



phi = 1.3
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_8 = nu



phi = 1.4
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_9 = nu



phi = 1.5
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_10 = nu

print(D_1)
print(D_2)
print(D_3)
print(D_4)
print(D_5)
print(D_6)
print(D_7)
print(D_8)
print(D_9)
print(D_10)
