import turtle
import math
for i in range(3,11):
	for j in range(i):
		turtle.left(180+180*(i-2)/i)
		turtle.forward(10+i*10)
	turtle.penup()
	turtle.forward(5)
	turtle.left(90)
	turtle.forward(5)
	turtle.right(90)
	turtle.pendown()

	
