import cantera as ct
import numpy as np

gas = ct.Solution("gri30.yaml")

#Unburned density
air = "O2:0.21,N2:0.79"
fuel_comp = "C3H8:0.3,NH3:0.7"
phi = 0.6
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
T = 300
P = 500000
gas.TP = T, P
rho = gas.density

#Burned
gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_1 = rho_ratio



phi = 0.7
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_2 = rho_ratio



phi = 0.8
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_3 = rho_ratio



phi = 0.9
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_4 = rho_ratio



phi = 1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_5 = rho_ratio



phi = 1.1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_6 = rho_ratio



phi = 1.2
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_7 = rho_ratio



phi = 1.3
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_8 = rho_ratio



phi = 1.4
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_9 = rho_ratio



phi = 1.5
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P
rho = gas.density

gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
rho_ratio = rho/rho_b

ratio_10 = rho_ratio


print(ratio_1)
print(ratio_2)
print(ratio_3)
print(ratio_4)
print(ratio_5)
print(ratio_6)
print(ratio_7)
print(ratio_8)
print(ratio_9)
print(ratio_10)