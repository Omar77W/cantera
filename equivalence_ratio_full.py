###### Open Anaconda program
###### Click Powershell Prompt or CMD.exe Prompt
###### Type "conda activate ct-env"
###### Type "jupyter lab"

###### Inside JupyterLab, type:


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
#gas.equilibrate('HP')   ###### Use 'HP' for adiabatic T and constant P, and use 'TP' for constant P and T, comment out for frozen properties
#gas()                 #### This is just to confirm the composition is correct
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

#DIJ = gas.binary_diff_coeffs # Binary diffusion coefficients
DI = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


#print('   Molar fractions '+str(gas.mole_fraction_dict()))
#print('   Density '+str(rho)+' (kg/m3)')
#print('   Mean molar mass '+str(Wgas)+' (kg/kmol)')
#print('   Gas constant '+str(Rgas)+' (kg/kmol)')
#print('   Enthalpy '+str(h/1e6)+' (MJ/kg)')
#print('   Energy '+str(u/1e6)+' (MJ/kg)')
#print('   Cp '+str(cp)+' (J/kg K)')
#print('   Cv '+str(cv)+' (J/kg K)')
#print('   Frozen Cp/Cv '+str(gamma_f)+' (m/s)')
#print('   viscosity '+str(mu)+' (kg/m s)')
#print('   viscosity (kinematic) '+str(nu)+' (m2/s)')
#print('   Thermal conductivity '+str(kcond)+' (W/m K)')
print('   Thermal diffusivity '+str(kdiff)+' (m2/s)')
#print('   Prandtl number '+str(Pr))
print('   ')

species = 'C3H8'
i_species = gas.species_index(species)

print('   Molar fraction of '+species+' '+str(gas.X[i_species]))
print('   Mixture mass diffusivity of '+species+' '+str(DI[i_species])+' (m2/s)')
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))
#print('   Schmidt number of '+species+' '+str(nu/DI[i_species]))
print('   ')

species = 'NH3'
i_species = gas.species_index(species)

print('   Molar fraction of '+species+' '+str(gas.X[i_species]))
print('   Mixture mass diffusivity of '+species+' '+str(DI[i_species])+' (m2/s)')
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))
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