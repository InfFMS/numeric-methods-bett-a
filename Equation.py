import math
import matplotlib.pyplot as plt
import numpy as np

def solve_equation(a, b, f, eps=0.001):
    while b - a >= 2 * eps:
        c = (a + b)/2
        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c

    return c

'''
def f1(x):
    return x**3 - x + 1
x = np.linspace(-10, 10, 1000)
plt.plot(x, f1(x))
plt.grid()
plt.xticks(np.linspace(-10, 10, 10))
plt.show()
print('Первое уравнение:', solve_equation(-2, -1, f1))  # -1.328125
'''

'''
def f2(x):
    return x**3 - x**2 - 9*x + 9
x = np.linspace(-10, 10, 1000)
plt.plot(x, f2(x))
plt.grid()
plt.show()
print('Второе уравнение: ', end='')      # -3.0125, 0.9875, 2.9875
print(solve_equation(-3.1, -2.9, f2), end=', ')
print(solve_equation(0.9, 1.1, f2), end=', ')
print(solve_equation(2.9, 3.1, f2))
'''

'''
def f3(x):
    return x**2 - math.e**x
x = np.linspace(-10, 10, 100)
plt.plot(x, f3(x))
plt.grid()
plt.show()
print(solve_equation(-2, 3, f3))   #-0.69140625
'''

'''
def f4(x):
    return 5 * x - 6 * np.log(x) - 7

x = np.linspace(-10, 10, 1000)
plt.plot(x, f4(x))
plt.grid()
plt.show()
print('Четвертое уравнение: ', end='')         #0.455078125, 2.498046875
print(solve_equation(0, 1, f4), end=', ')
print(solve_equation(2, 3, f4))
'''

'''
def f5(x):
    return np.cos(x) + 2 * x - 3
x = np.linspace(-10, 10, 100)
plt.plot(x, f5(x))
plt.grid()
plt.show()
print('Пятое уравнение:', solve_equation(1, 2, f5))    #1.427734375
'''


