import turtle

def draw_a():
	window = turtle.Screen()
	window.bgcolor("blue")

 	letter = turtle.Turtle()
	letter.speed(2)

	# letter A
	letter.pu()
	letter.setpos(10, 0)
	letter.pd()
	letter.left(120)
	letter.forward(100)
	letter.left(120)
	letter.forward(100)
	letter.right(180)
	letter.forward(50)
	letter.right(60)
	letter.forward(50)
	print (letter.pos())

	# letter B
	letter.pu()
	letter.setpos(20, 0)
	letter.pd()
	letter.left(90)
	letter.forward(100)
	letter.right(180)
	letter.forward(50)
	letter.left(90)
	letter.forward(60)
	letter.left(90)
	letter.forward(50)
	letter.right(180)
	letter.forward(100)

	window.exitonclick()

draw_a()