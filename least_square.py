import numpy as np
import matplotlib.pyplot as plt

data = np.array([[1, 0],[2, 0],[3, 0],[4, 1],[5, 1],[10, 1],[11, 1],[12, 1],[13, 1]])

def divide_data(list):
    x = list[:,[0]]
    y = list[:,[1]]
    plt.scatter(x, y)
    plt.show()
    return x, y

def linear_reg(x, y):
    xsum = 0
    ysum = 0
    m_num = 0
    m_den = 0
    m = 1
    b = 0
    y_pred = 0
    for i in range(len(x)):
        xsum += x[i]
        ysum += y[i]

    xmean = xsum/(len(x))
    ymean = ysum/(len(y))
    for i in range(len(x)):
        m_num = (x[i] - xmean) * (y[i] - ymean)
        m_den = (x[i] - xmean) * (x[i] * xmean)
    m = m_num/m_den
    b = ymean - m * xmean
    print("slope : " +  str(m))
    print("y- intercept : " +  str(b))
    y_pred = m * xmean + b
    y_p = []
    for j in range(len(x)):
        y_p.append(y_pred)

    plt.scatter(x, y, color='green')
    plt.scatter(x, y_p, color='red')
    plt.plot([min(x), max(x)], [min(y_p), max(y_p)], color='red')
    #test data
    test = np.array([[2.4, 0], [5.5, 1], [3.9, 0]])
    test_result = divide_data(test)
    test_x = test_result[0]
    test_y = test_result[1]
    plt.scatter(test_x, test_y, color='black')
    plt.plot([min(x), max(x)], [min(y_p), max(y_p)], color='red')
    plt.show()

result = divide_data(data)
x = result[0]
y = result[1]

linear_reg(x, y)
