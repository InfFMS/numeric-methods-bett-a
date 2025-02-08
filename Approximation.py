import numpy as np
import matplotlib.pyplot as mpl

i = np.array([0.1, 0.311, 0.522, 0.733, 0.944, 1.156, 1.367, 1.578, 1.789, 2.0])
u = np.array([0.599, 1.528, 2.741, 3.971, 4.675, 5.731, 7.149, 8.042, 8.851, 10.109 ])

sum = 0
A = 0
for j in range(len(i)):
    sum += i[j] * u[j]
    A += (i[j])**2
B = 2 * sum
r = B/(2 * A)


# прямая сопротивления
I = np.linspace(0.1, 2.0, 10)
U = [I*r for i in I]
mpl.plot(I, I*r, color='gray')
mpl.xlabel('Значения U')
mpl.ylabel('Значения I')
mpl.scatter(i, u, color='red')
mpl.show()