import cantera as ct
import numpy as np

## Functions
# Get diffusion coefficients from multicomponent ones  
def diffusion_coefficients_from_multicomponent(gas):
    multi_diffusion_coefficients = gas.multi_diff_coeffs
    meanM = gas.mean_molecular_weight
    new_diff = np.zeros(gas.n_species)
    for k in range(gas.n_species):
        sum = 0.0
        for j in range(gas.n_species):
            if j != k: sum += gas.X[j]/multi_diffusion_coefficients[j,k]    
        new_diff[k] = (meanM - gas.X[k]*gas.molecular_weights[k]) / (meanM*sum)
    return new_diff


## Input data
Ru = ct.gas_constant
gas = ct.Solution('gri30.yaml')

air = "O2:0.21,N2:0.79"
fuel_comp = "NH3:0.5,C3H8:0.5"
phi = 1
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
gas.transport_model = 'Multi' # simple mixture average transport model 
T = 300
P = 100000
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

DI = diffusion_coefficients_from_multicomponent(gas)

species = 'NH3'
i_species = gas.species_index(species)
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))

species = 'O2'
i_species = gas.species_index(species)
print('   Lewis number of '+species+' '+str(kdiff/DI[i_species]))