import matplotlib.pyplot as plt
import numpy as np
x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
t=np.arange(0,10,0.1)
p=np.polyfit(x,y,deg=1)
p1=np.polyfit(x,y,deg=2)
for i in range(5):
	plt.errorbar(x[i],y[i],xerr=(x[i]*0.05),yerr=(y[i]**2-y[i]))
plt.errorbar(x, y)
p_f=np.poly1d(p)
plt.plot(t,p_f(t))
p_f=np.poly1d(p1)
plt.plot(t,p_f(t))
plt.grid()
plt.show()
