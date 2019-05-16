import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('populacje.txt')
plt.plot(data)
plt.show()
