import turtle
turtle.begin_fill()
turtle.color('green')
for j in range(360):
	turtle.forward(3)
	turtle.left(1)
turtle.end_fill()
turtle.goto(-50,250)
turtle.begin_fill()
turtle.color('blue')
for j in range(360):
	turtle.forward(0.5)
	turtle.left(1)
turtle.end_fill()
turtle.penup()
turtle.goto(50,250)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
for j in range(360):
	turtle.forward(0.5)
	turtle.left(1)
turtle.end_fill()
turtle.penup()
turtle.goto(0,200)
turtle.pendown()
turtle.right(90)
turtle.color('red')
turtle.width(20)
turtle.forward(100)
turtle.penup()
turtle.goto(-50,100)
turtle.pendown()
turtle.color('yellow')
for j in range(180):
	turtle.forward(1)
	turtle.left(1)



