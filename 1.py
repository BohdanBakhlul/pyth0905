import matplotlib.pyplot as plt
import numpy as np

X = np.load('x.npy')
Y = np.load('y.npy')
X1 = np.linspace(0, 1, 1000)
A = np.polyfit(X, Y, 1)
B = np.polyfit(X, Y, 2)
C = np.polyfit(X, Y, 10)
p = np.poly1d(A)
q = np.poly1d(B)
r = np.poly1d(C)
plt.plot(X, Y, '.')
plt.plot(X1, p(X1), '.')
plt.plot(X1, r(X1), '--')
plt.plot(X1, q(X1))
plt.show()
