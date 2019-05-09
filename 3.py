import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


Z = np.loadtxt('PCAdata.txt')
B = np.cov(Z)
w, v = (np.linalg.eig(B))
print(w)
print(v)
