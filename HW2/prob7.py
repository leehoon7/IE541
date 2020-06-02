import csv
import numpy as np
import matplotlib.pyplot as plt


def main():

    full_data = []
    with open('fiji_.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            for data in row:
                full_data.append(float(data))

    mag = np.array(full_data)
    maxi = mag.max()
    mini = mag.min()
    epsilon = np.sqrt((1/2000) * np.log(2/0.1))

    print('epsilon : {}'.format(epsilon))
    print('minimum : {}, maximum : {}'.format(mini, maxi))

    x = np.linspace(mini, maxi, (maxi-mini)/0.1 + 1)
    y = []
    y_u = []
    y_l = []

    for i in x:
        y.append(sum(mag <= i)/1000)
        y_u.append(min([y[-1]+epsilon, 1.0]))
        y_l.append(max([y[-1]-epsilon, 0.0]))

        if float(i) == 4.5 :
            print(y[-1], i, y_l[-1], y_u[-1])
        if float(i) == 5.0 :
            print(y[-1], i, y_l[-1], y_u[-1])

    plt.plot(x, y)
    plt.xlabel('mag')
    plt.ylabel('cdf')
    plt.fill_between(x, y_u, y_l, alpha=0.2)
    plt.savefig('prob7.png')
    plt.show()



if __name__ == '__main__':
    main()