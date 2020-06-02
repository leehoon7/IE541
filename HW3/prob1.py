import random

random.seed(2020)

data = []
for i in range(10):
    data.append(random.random() * 2 + 1)

tau_c = (min(data) + max(data)) / 2
mse1 = (tau_c - 2) ** 2
print(mse1)

mse2 = ((3 - 1) ** 2) / 120
print(mse2)