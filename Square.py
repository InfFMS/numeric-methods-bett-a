import matplotlib.pyplot as plt
import numpy as np
pi = np.pi
e = np.e

def f11(x):
    return np.sin(2 * x) + 1
def f12(x):
    return -0.2 * x**2 + 0.5

def f21(x):
    return np.cos(x) + 1.2
def f22(x):
    return -0.5 * x**2 + 0.7

def f31(x):
    return e**-(x**(2)) + 0.5
def f32(x):
    return 0.2 * np.sin(3*x) - 0.5

def f41(x):
    return e**(-(x + 1)**2) + e**(-(x-1)**2)
def f42(x):
    return -0.3 * x**2

def graph(a, b, f1, f2):
    x = np.linspace(a, b, 100)
    plt.plot(x, f1(x), color='blue')
    plt.plot(x, f2(x), color='orange')
    plt.show()
def area(a, b, f, n = 100):
    area = 0
    dx =  (b - a)/(n - 1)
    for i in range(n - 1):
        x1 = a + i * dx
        y1 = f(x1)
        x2 = a + (i + 1) * dx
        y2 = f(x2)
        area += 0.5 * (y1 + y2) * (x2 - x1)

    return area

#print('Площадь первой фигуры:', area(0, pi, f11) - area(0, pi, f12))  # 3.637986891580524
#graph(0, pi, f11, f12)

#print('Площадь второй фигуры:', area(-pi/2, pi/2, f21) - area(-pi/2, pi/2, f22))  # 4.8628203176154745
#graph(-pi/2, pi/2, f21, f22)

#print('Площадь третьей фигуры:', area(-2, 2, f31) - area(-2, 2, f32))  # 5.764142853593164
#graph(-2, 2, f31, f32)

print('Площадь четвертой фигуры:', area(-2, 2, f41) - area(-2, 2, f42))  # 4.8661890611755965
graph(-2, 2, f41, f42)






