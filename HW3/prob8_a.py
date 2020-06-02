
x = [0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217]
y = [0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201]

x_bar = sum(x)/len(x)
y_bar = sum(y)/len(y)

print(x_bar, y_bar)

std_x = 0
std_y = 0

for x_ in x:
    std_x += (x_ - x_bar) ** 2

for y_ in y:
    std_y += (y_ - y_bar) ** 2

std_x = (std_x / (len(x) - 1)) ** 0.5
std_y = (std_y / (len(y) - 1)) ** 0.5

print(std_x, std_y)

delta = x_bar - y_bar
std_delta = (((std_x ** 2) / len(x)) + ((std_y ** 2) / len(y))) ** 0.5

print(delta, std_delta)

W = delta / std_delta

print(W, 1.96)