import cantera as ct
## Input data
Ru = ct.gas_constant
transport = 'Mix' # simple mixture average transport model 
gas = ct.Solution('burke_plus_okafor.yaml')

air = "O2:0.21,N2:0.79"
fuel_comp = "C3H6:0.3,NH3:0.7"
T = 300
P = 500000


phi = 0.6
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_1 = kcond/(rho*cp)
DI_1 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients



phi = 0.7
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_2 = kcond/(rho*cp)
DI_2 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


phi = 0.8
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_3 = kcond/(rho*cp)
DI_3 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


phi = 0.9
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_4 = kcond/(rho*cp)
DI_4 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


phi = 1.1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_5 = kcond/(rho*cp)
DI_5 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


phi = 1.2
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_6 = kcond/(rho*cp)
DI_6 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


phi = 1.3
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_7 = kcond/(rho*cp)
DI_7 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


phi = 1.4
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_8 = kcond/(rho*cp)
DI_8 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


phi = 1.5
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.TP = T, P

## Compute properties at T and P
rho = gas.density
Wgas = gas.mean_molecular_weight
Rgas = Ru/Wgas
h = gas.enthalpy_mass
u = gas.int_energy_mass
cp = gas.cp_mass
cv = gas.cv_mass
gamma_f = cp/cv
mu = gas.viscosity
nu = mu/rho
kcond = gas.thermal_conductivity
Pr = mu*cp/kcond;

kdiff_9 = kcond/(rho*cp)
DI_9 = gas.mix_diff_coeffs      # Mixture diffusion Coefficients





species = 'NH3'
i1_species = gas.species_index(species)
species = 'C3H6'
i2_species = gas.species_index(species)
species = 'O2'
i3_species = gas.species_index(species)



print(0.7*(kdiff_1/DI_1[i1_species])+0.3*(kdiff_1/DI_1[i2_species]))
print(0.7*(kdiff_2/DI_2[i1_species])+0.3*(kdiff_2/DI_2[i2_species]))
print(0.7*(kdiff_3/DI_3[i1_species])+0.3*(kdiff_3/DI_3[i2_species]))
print(0.7*(kdiff_4/DI_4[i1_species])+0.3*(kdiff_4/DI_4[i2_species]))
print(kdiff_5/DI_5[i3_species])
print(kdiff_6/DI_6[i3_species])
print(kdiff_7/DI_7[i3_species])
print(kdiff_8/DI_8[i3_species])
print(kdiff_9/DI_9[i3_species])