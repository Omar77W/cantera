###### Open Anaconda program
###### Click Powershell Prompt or CMD.exe Prompt
###### Type "conda activate ct-env"
###### Type "jupyter lab"

###### Inside JupyterLab, type:


import cantera as ct

## Input data
Ru = ct.gas_constant
q = 'O2:190 N2:715 CH4:95'   # Air and fuel molar fraction or partial pressures
transport = 'Mix' # simple mixture average transport model 
gas = ct.Solution('gri30.yaml')


## Compute properties at T P and q
T = 300
P = 100000   # in Pascal
gas.TPX = T,P,q
#gas.equilibrate('HP')   ###### Use 'HP' for adiabatic T and constant P, and use 'TP' for constant P and T, comment out for frozen properties
gas()                 #### This is just to confirm the composition is correct
print('Computing  properties for '+q+'')
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


species = 'CH4'      ##### Specify species
i_species = gas.species_index(species)
#DIJ = gas.binary_diff_coeffs # Binary diffusion coefficients
DI = gas.mix_diff_coeffs      # Mixture diffusion Coefficients


#print('   Pressure '+str(P/1e3)+' (kPa)')
#print('   Temperature '+str(T)+' (K)')
print('   Density '+str(rho)+' (kg/m3)')
print('   Mean molar mass '+str(Wgas)+' (kg/kmol)')
print('   Gas constant '+str(Rgas)+' (kg/kmol)')
print('   Enthalpy '+str(h/1e6)+' (MJ/kg)')
print('   Energy '+str(u/1e6)+' (MJ/kg)')
print('   Cp '+str(cp)+' (J/kg K)')
print('   Cv '+str(cv)+' (J/kg K)')
print('   Frozen Cp/Cv '+str(gamma_f)+' (m/s)')
print('   viscosity '+str(mu)+' (kg/m s)')
print('   viscosity (kinematic) '+str(nu)+' (m2/s)')
print('   thermal conductivity '+str(kcond)+' (W/m K)')
print('   thermal diffusivity '+str(kdiff)+' (m2/s)')
print('   Prandtl number '+str(Pr))
print('   Mixture mass diffusivity of '+species+' '+str(DI[i_species])+' (m2/s)')
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))
print('   Schmidt number of '+species+' '+str(nu/DI[i_species]))
i_N2 = gas.species_index('N2')
print('   Mixture mass diffusivity of '+'N2'+' '+str(DI[i_N2])+' (m2/s)')
print('   Lewis number of '+'N2'+' '+str(kdiff/DI[i_N2]))
print('   Schmidt number of '+'N2'+' '+str(nu/DI[i_N2]))
print('   ')

