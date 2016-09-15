import turtle
for i in range(5):
	for j in range(361):
		turtle.forward(1+i*0.1)
		turtle.left(1)
	for g in range(361):
		turtle.right(1)
		turtle.forward(1+i*0.1)
