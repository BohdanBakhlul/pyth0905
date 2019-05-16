import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('populacje.txt')
a = np.mean(data[0])
b = np.mean(data[1])
c = np.mean(data[2])
print(a)
print(b)
print(c)
plt.plot(data)
plt.show()
