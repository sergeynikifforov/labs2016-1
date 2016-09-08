import numpy as np
import matplotlib.pyplot as plt
q=0
a=int(input())
b=float(input())
if a%2==0 or a==1:
	print('1 4ucJIo goJI}I{HO 6bItb He4eTHbIM u HePaBHo 1')
elif b>=1 or b<0:
	print('2 4ucJIo goJI}I{HO 6bItb <1')
else:
	x = np.arange(0,10.01,0.01)
	for n in range(100):
    		q+=b**n*np.cos(a**n*np.pi*x)
	plt.plot(x,q)
	plt.grid(True)
	plt.show()

