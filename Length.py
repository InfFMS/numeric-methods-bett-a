import matplotlib.pyplot as plt
import numpy as np
from math import pi

def f1(x):
    return np.cos(x)

def f2(x):
    return np.cos(x) + 0.1 * x**2

def f3(x):
    return -np.tan(x - pi/2)

def f4(x):
    return -0.2 * (x - pi)**3 + 0.5 * (x - pi)**2 + 1