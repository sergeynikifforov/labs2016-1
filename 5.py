import numpy as np
import matplotlib.pyplot as plt
plt.xkcd()
x = np.arange(-10,10.01, 0.01)
plt.plot(x,eval(input()))
plt.grid(True)
plt.show()
