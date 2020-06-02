import numpy as np

np.random.seed(seed = 2020)

B = 10000
psi = []
z = 1.645

x1 = np.random.binomial(200, 0.8, B)
x2 = np.random.binomial(200, 0.74, B)

psi = (x1 - x2)/200
psi_mean = np.mean(psi)
print(psi_mean)

std = 0
for b in range(B):
    std += (psi[b] - psi_mean)**2
std = (std / B) ** 0.5
print(std)

print(psi_mean - z * std, psi_mean + z * std)