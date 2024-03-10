import cantera as ct
import numpy as np

gas = ct.Solution("gri30.yaml")

air = "O2:0.21,N2:0.79"
fuel_comp = "C3H8:0.3,NH3:0.7"
phi = 1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
T = 300
P = 100000
gas.TP = T, P
nu = gas.viscosity/gas.density    # kinematic viscosity

D_1 = nu



P = 150000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_2 = nu



P = 200000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_3 = nu



P = 250000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_4 = nu


P = 300000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_5 = nu


P = 350000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_6 = nu



P = 400000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_7 = nu


P = 450000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_8 = nu



P = 500000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_9 = nu



P = 550000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_10 = nu



P = 600000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_11 = nu



P = 650000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_12 = nu



P = 700000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_13 = nu



P = 750000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_14 = nu



P = 800000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_15 = nu



P = 850000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_16 = nu



P = 900000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_17 = nu



P = 950000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_18 = nu



P = 1000000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_19 = nu



P = 1050000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_20 = nu



P = 1100000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_21 = nu



P = 1150000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_22 = nu


P = 1200000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_23 = nu


P = 1250000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_24 = nu



P = 1300000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_25 = nu



P = 1350000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_26 = nu



P = 1400000
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
nu = gas.viscosity/gas.density

D_27 = nu


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
print(D_11)
print(D_12)
print(D_13)
print(D_14)
print(D_15)
print(D_16)
print(D_17)
print(D_18)
print(D_19)
print(D_20)
print(D_21)
print(D_22)
print(D_23)
print(D_24)
print(D_25)
print(D_26)
print(D_27)
