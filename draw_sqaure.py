import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("blue")

    nilson = turtle.Turtle()
    nilson.speed(10)
    for i in range (1, 37):
        for i in range (1, 5):
            nilson.forward(100)
            nilson.right(90)
        nilson.right(10)

    window.exitonclick()

draw_square()