import turtle


import turtle

window = turtle.Screen()
window.bgcolor("white")



def draw_intials():
	window = turtle.Screen()
	window.bgcolor("purple")

	p1 = turtle.Turtle()

	p1.left(120)
	p1.forward(100)
	p1.left(120)
	p1.forward(100)
	p1.right(180)
	p1.forward(50)
	p1.right(50)
	p1.forward(50)
	window.exitonclick()
draw_intials()



def draw_square():

	window = turtle.Screen()
	window.bgcolor("red")

	pointer = turtle.Turtle()
	pointer.shape("turtle")
	pointer.color("black", "green")
	pointer.speed(0)
	
	outside_count = 1
	while outside_count <= 40:
		inside_count = 1
		while inside_count<=4:
			pointer.forward(100)
			pointer.right(90)
			inside_count = inside_count + 1
		pointer.right(10)
		outside_count = outside_count + 1

	pointer2 = turtle.Turtle()
	pointer2.shape("square")
	pointer2.color("blue")
	pointer2.speed("10")
	pointer2.circle(100)

	pointer3 = turtle.Turtle()
	pointer3.shape("triangle")
	pointer3.color("yellow")
	pointer3.speed("6")
	pointer3.forward(100)
	pointer3.right(90)
	pointer3.forward(100)
	pointer3.right(135)
	pointer3.forward(130)

	
	window.exitonclick()

draw_square()