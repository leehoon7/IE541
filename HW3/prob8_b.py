import random
import numpy as np

random.seed(2020)
x = [0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217]
y = [0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201]
T = sum(x)/len(x) - sum(y)/len(y)
data = x + y

B = 1000
T_list = []

for _ in range(B):
    random.shuffle(data)

    x_bar = np.mean(data[:8])
    y_bar = np.mean(data[8:])

    t = abs(x_bar - y_bar)
    T_list.append(t)

cnt = 0
for i in range(B):
    if T_list[i] > T:
        cnt += 1
p_value = cnt/B

print('# of case : ', cnt)
print('p-value   : ', p_value)