import cantera as ct
## Input data
Ru = ct.gas_constant
transport = 'Mix' # simple mixture average transport model 
gas = ct.Solution('gri30.yaml')

air = "O2:0.21,N2:0.79"
fuel_comp = "C3H8:0.3,NH3:0.7"
gas.set_equivalence_ratio(phi=0.6, fuel=fuel_comp, oxidizer=air)


## Compute properties at T and P
T = 300
P = 500000
gas.TP = T, P
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
print('   ')

species = 'NH3'
i_species = gas.species_index(species)

print('   Molar fraction of '+species+' '+str(gas.X[i_species]))
print('   Mixture mass diffusivity of '+species+' '+str(DI[i_species])+' (m2/s)')
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))
print('   ')

species = 'C3H8'
i_species = gas.species_index(species)

print('   Molar fraction of '+species+' '+str(gas.X[i_species]))
print('   Mixture mass diffusivity of '+species+' '+str(DI[i_species])+' (m2/s)')
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))
#print('   Schmidt number of '+species+' '+str(nu/DI[i_species]))
print('   ')

species = 'O2'
i_species = gas.species_index(species)

print('   Molar fraction of '+species+' '+str(gas.X[i_species]))
print('   Mixture mass diffusivity of '+species+' '+str(DI[i_species])+' (m2/s)')
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))
print('   ')

species = 'N2'
i_species = gas.species_index(species)

print('   Molar fraction of '+species+' '+str(gas.X[i_species]))
print('   Mixture mass diffusivity of '+species+' '+str(DI[i_species])+' (m2/s)')
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))
print('   ')