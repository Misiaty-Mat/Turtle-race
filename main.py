from turtle import Turtle, Screen
from random import randint

# setup
screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

# getting user input
user_input = screen.textinput(
    title=f"Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]


# startting race
if user_input:
    is_race_on = True

# turtles setup
x_axis = -190
y_axis = -120
color_index = 0
turtles = []
for turtle_index in range(0, 6):
    turt = Turtle(shape="turtle")
    turt.color(turtle_colors[color_index])
    color_index += 1

    turt.penup()

    turt.goto(x=x_axis, y=y_axis)
    y_axis += 50

    turtles.append(turt)


# race management code
while is_race_on:
    for turt in turtles:
        rand_distance = randint(0, 10)
        turt.forward(rand_distance)
        if turt.xcor() > 230:
            is_race_on = False
            winning_color = turt.pencolor()
            if winning_color == user_input:
                print(f"The winner was {winning_color}. You bet right!")
            else:
                print(f"The winner was {winning_color}. You bet wrong!")


screen.exitonclick()
