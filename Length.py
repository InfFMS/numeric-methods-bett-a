import matplotlib.pyplot as plt
import numpy as np

def lenth(f):
    x = np.linspace(0, np.pi, 100)
    plt.plot(x, f(x))
    plt.grid()
    plt.show()
    sum = 0
    for i in range(len(x) - 1):
        x1 = x[i]
        y1 = f(x1)
        x2 = x[i+1]
        y2 = f(x2)
        sum += ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return sum

def f1(x):
    return np.cos(x)

def f2(x):
    return np.cos(x) + 0.1 * x**2

def f3(x):
    return -1 * np.tan(x - np.pi/2)

def f4(x):
    return -1 * 0.2 * (x - np.pi)**3 + 0.5*(x - np.pi)**2 + 1

#print(lenth(f1))    # 3.820147518333091
#print(lenth(f2))    # 3.4777354304632864
#print(lenth(f3))    # 3.2662478706390732e+16
#print(lenth(f4))    #11.984164397173986