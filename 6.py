import turtle
n=int(input())
for i in range(n+1):
	turtle.forward(50)
	turtle.stamp()
	turtle.backward(50)
	turtle.left(360/n)	
