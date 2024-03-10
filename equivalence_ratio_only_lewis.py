import cantera as ct
## Input data
Ru = ct.gas_constant
transport = 'Mix' # simple mixture average transport model 
gas = ct.Solution('gri30.yaml')

air = "O2:0.21,N2:0.79"
fuel_comp = "C3H8:0.5,NH3:0.5"
phi = 0.7
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
T = 300
P = 750000
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
kdiff = kcond/(rho*cp)
Pr = mu*cp/kcond;

DI = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


print('   Thermal diffusivity '+str(kdiff)+' (m2/s)')

species = 'NH3'
i_species = gas.species_index(species)
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))

species = 'C3H8'
i_species = gas.species_index(species)
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))

species = 'O2'
i_species = gas.species_index(species)
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))

# Compute burned properties
gas_b = ct.Solution('gri30.yaml')
gas_b.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas_b.TP = T, P
gas_b.equilibrate('HP')
rho_b = gas_b.density
T_b = gas_b.T
rho_ratio = rho/rho_b
temp_ratio = T_b/T

gas3 = ct.Solution('gri30.yaml')  #Thermal conductivity at T_b
gas3.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas3.TP = T_b, P
kcond_at_b = gas3.thermal_conductivity

print('   Density ratio '+str(rho_ratio))
print('   Thermal conductivity at T_b '+str(kcond_at_b))
print('   Temperature ratio '+str(temp_ratio))