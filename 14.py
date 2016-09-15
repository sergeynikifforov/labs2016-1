import turtle
def f(n):
	for i in range(1,n+1):
		turtle.forward(100)
		turtle.right(180-180/n)
f(5)
turtle.penup()
turtle.goto(300,0)
turtle.pendown()
f(11)
	
