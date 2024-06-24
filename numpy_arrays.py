import numpy as np
fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])
m = np.mean(fluxes)
print(m)
print(f'np.size(fluxes): {np.size(fluxes)}')
print(f'np.std(fluxes): {np.std(fluxes)}')