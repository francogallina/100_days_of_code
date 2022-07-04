import turtle
from turtle import Turtle, Screen
from random import randint
tim = Turtle()
tim.shape("turtle")

turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b
#
# directions = [0, 90, 180, 270]
#
# tim.pensize(10)
# tim.speed(0)
# for i in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(choice(directions))


tim.speed(0)
for i in range(int(360/5)):
    tim.color(random_color())
    tim.circle(100, 360)
    tim.right(5)

screen = Screen()
screen.exitonclick()
