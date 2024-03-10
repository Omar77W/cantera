import math
import matplotlib.pyplot as plt
import numpy as np
import cantera as ct

gas = ct.Solution("gri30.yaml")

air = "O2:0.21,N2:0.79"
fuel_comp = "C3H8:0,NH3:1"
phi = 1.0
gas.set_equivalence_ratio(phi=phi, fuel=fuel_comp, oxidizer=air)
T = 300
P = 500000
gas.TP = T, P
Pr = 0.7
Le_eff = 1.25   #Change according to composition
rho = gas.density
lambda_u = gas.thermal_conductivity

gas.equilibrate('HP')
T_b = gas.T
lambda_b = (T_b/T)**0.5
#lambda_b = T**0.5
#lambda_b = gas.thermal_conductivity
#lambda_b = 1
rho_b = gas.density

sigma = rho / rho_b


E_a = 177000


beta = (E_a * (T_b - T)) / (ct.gas_constant * (T_b)**2)

def compute_Pe(sigma, n, lambda_b, Le_eff, beta, Pr):
    # Compute coefficients a, b, c
    a = (sigma + 1) * n + 1
    b = 2 * n**2 + (4 + 5 * sigma) * n + 4
    c = -((sigma - 1) / sigma) * n**3 + 2 * n**2 + (3 * (sigma + 1) - 1 / sigma) * n + 2

    gamma_1 = (sigma / (sigma - 1)) * lambda_b * math.log(abs(sigma))
    gamma_2 = -lambda_b / (2 * (sigma - 1)) * math.log((sigma - 1) / (sigma - 2))**2
    gamma_3 = lambda_b

    # Calculate omega
    omega = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

    #Calcualte delta
    delta = (2 * a * omega) + b - (2 * a)

    # Calculate Q1
    Q1 = (gamma_1 / (sigma * delta)) * (
        n**4 * (sigma + 1) + sigma * n**3 * (2 * omega + 5) +
        n**2 * (omega * sigma - 2 * sigma**2 + sigma - 1) +
        n * sigma * (sigma - 7 - 3 * omega - sigma * omega) - 2 * sigma * (1 + omega)) + (gamma_3 / (sigma * delta)) * (n * (n**2 - 1) * (n + 2) * (sigma - 1))

    # Calculate Q2
    Q2 = (gamma_2 * (sigma - 1) / (2 * delta)) * (
        2 * n**4 + n**3 * (2 * omega * sigma + 2 * omega + 10 * sigma - 3) +
        n**2 * (2 * sigma * omega**2 + (5 * sigma - 1) * omega + 3 * sigma - 2 * sigma**2 - 2) +
        n * (sigma * omega**2 * (1 - 4 * sigma) - (14 * sigma**2 + 1) * omega + 3 - 9 * sigma - 8 * sigma**2) -
        2 * sigma * (omega**2 + 4 * omega + 3))

    # Calculate Q3
    Q3 = (2 * n * (n**2 - 1) * (sigma - 1) / (sigma * delta)) * ((n + 2) * (lambda_b - gamma_3) - 3 * (lambda_b - 1))

    # Calculate Pe
    Pe = (Q1 + (beta * (Le_eff - 1) / (sigma - 1)) * Q2 + Pr * Q3) / omega

    return Pe


# Generate an array of n values
n_values = np.linspace(7, 120, 1000)  # Adjust the range and number of points as needed

# Compute Pe values for each n
Pe_values = [compute_Pe(sigma, n, lambda_b, Le_eff, beta, Pr) for n in n_values]


# Plot the results
plt.plot(Pe_values, n_values, label='n as a function of Pe')
plt.xlabel('Pe')
plt.ylabel('n')
plt.xlim([0,1100])
plt.title('Plot of n as a function of Pe')
plt.legend()
plt.grid(True)
plt.show()
