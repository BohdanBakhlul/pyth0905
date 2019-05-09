import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

Z = np.loadtxt('PCAdata.txt')
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(Z[0], Z[1], Z[2], '.')

plt.show()
print(np.mean(Z))
print(np.cov(Z))
