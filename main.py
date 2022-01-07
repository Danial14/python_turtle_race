# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width = 500, height = 400)
color = ["red", "green", "blue", "purple", "yellow", "orange"]
userInput = screen.textinput(title = "Choose your turtle", prompt = "Which turtle will win the race")
if userInput:
   userInput = userInput.lower()
turtles = []
race_is_on = True
y_axis = 80

for i in range(0, 6):
    tim = Turtle(shape = "turtle")
    tim.color(color[i])
    tim.penup()
    y_axis = y_axis - 30
    tim.goto(-240, y_axis)
    turtles.append(tim)

while race_is_on:
    for i in range(0, 6):
        turtle = turtles[i]
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 230:
            if userInput == turtle.fillcolor():
                print("You win")
            else:
                print(f"{turtle.fillcolor()} turtle win")
            race_is_on = False
            break





screen.exitonclick()
