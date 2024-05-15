from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

tam = Turtle()
tam.color("CadetBlue2")
tam.shape("turtle")
tam.penup()
tam.goto(x=-230, y=-100)

tem = Turtle()
tem.color("DarkMagenta")
tem.shape("turtle")
tem.penup()
tem.goto(x=-230, y=-50)

tim = Turtle()
tim.color("DarkSlateBlue")
tim.shape("turtle")
tim.penup()
tim.goto(x=-230, y=0)

tom = Turtle()
tom.color("DarkOrchid")
tom.shape("turtle")
tom.penup()
tom.goto(x=-230, y=50)

tum = Turtle()
tum.color("DeepPink3")
tum.shape("turtle")
tum.penup()
tum.goto(x=-230, y=100)
all_turtles = [tim, tom, tam, tem, tum]

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
