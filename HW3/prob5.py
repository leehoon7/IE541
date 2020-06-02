import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(2020)
np.random.seed(seed=2020)
data = np.random.normal(5, 1, size=100)
z = 1.96

# delta method
n = 100
x_bar = np.mean(data)
exp_x = np.exp(x_bar)
std = exp_x / (n ** 0.5)

print(exp_x - z * std, exp_x + z * std)

# parametric bootstrap
mu = np.mean(data)
sig = 0
B = 100
for i in range(n):
    sig += (data[i] - mu) ** 2
sig = (sig / (n - 1)) ** 0.5

bootstrap = []
for b in range(B):
    new_data = np.random.normal(mu, sig, size=100)
    mu_star = np.mean(new_data)
    tau_star = np.exp(mu_star)
    bootstrap.append(tau_star)

tau_mean = np.mean(bootstrap)
std_boot = 0
for b in range(B):
    std_boot += (bootstrap[i] - tau_mean) ** 2
std_boot = (std_boot / B) ** 0.5
print(tau_mean - z * std_boot, tau_mean + z * std_boot)


# nonparametric bootstrap
n_small = 80
bootstrap_non = []

for b in range(B):
    new_data = random.choices(data, k=n_small)
    tau_star_ = np.exp(np.mean(new_data))
    bootstrap_non.append(tau_star_)

mean_boot = np.mean(bootstrap_non)
std_boot_ = 0
for b in range(B):
    std_boot_ += (bootstrap_non[b] - mean_boot) ** 2
std_boot_ = (std_boot_ / B) ** 0.5

print(mean_boot - z * std_boot_, mean_boot + z * std_boot_)


#plot_data = np.array([data, bootstrap, bootstrap_non])
#print(np.shape(plot_data))
e_data = []
d_data = []
for i in range(100):
    new_data = np.random.normal(5, 1, size=100)
    e_data.append(np.exp(np.mean(new_data)))

    new_data = np.random.normal(mu, sig, size=100)
    d_data.append(np.exp(np.mean(new_data)))

hist_data = np.array([e_data, d_data, bootstrap, bootstrap_non])
print(np.size(hist_data))

bins = np.linspace(110, 210, 20)
name = ['delta', 'parametric_bootstrap', 'nonparametric_bootstrap']
for i in range(3):
    hist = plt.hist(e_data, bins=bins, alpha=1, stacked=True, label='true dist')
    if i == 0:
        hist = plt.hist(d_data, bins=bins, alpha=0.5, color='red', stacked=True, label='delta')
    elif i == 1:
        hist = plt.hist(bootstrap, bins=bins, alpha=0.5, color='red', stacked=True, label='param bootstrap')
    elif i == 2:
        hist = plt.hist(bootstrap_non, bins=bins, alpha=0.5, color='red', stacked=True, label='nonparam bootstrap')
    plt.legend(loc = 'upper right')
    plt.savefig('prob5-b-' + name[i] + '.png')
    plt.close()


hist = plt.hist(e_data, bins=bins, alpha=1, stacked=True, label='true dist')
hist = plt.hist(d_data, bins=bins, alpha=0.5, stacked=True, label='delta')
hist = plt.hist(bootstrap, bins=bins, alpha=0.5, stacked=True, label='param bootstrap')
hist = plt.hist(bootstrap_non, bins=bins, alpha=0.5, stacked=True, label='nonparam bootstrap')
plt.legend(loc='upper right')
plt.savefig('prob5-b.png')
