import turtle
turtle.penup()
turtle.goto(0,-50)
turtle.pendown()
turtle.shape('turtle')
turtle.begin_fill()
turtle.color('red')
for i in range(361):
	turtle.forward(2)
	turtle.left(1)
turtle.end_fill()
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color('black')
turtle.width(10)
turtle.shape('turtle')
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.goto(0,100)
turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)


