from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?: Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,(-100+i*50))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 230:
            turtle_win = turtle.color()
            is_race_on = False
if turtle_win == user_bet:
    print(f"You win. The turtle winner is {turtle_win[0]}")
else:
    print(f"You lose. The turtle winner is {turtle_win[0]}")


screen.exitonclick()
