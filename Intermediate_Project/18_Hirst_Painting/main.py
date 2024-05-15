colour_list = [(240, 235, 230), (214, 155, 106), (206, 136, 159), (240, 208, 224), (131, 171, 201), (212, 222, 239), (223, 200, 124), (212, 233, 219), (192, 152, 38), (138, 182, 157), (234, 164, 185), (202, 86, 112), (170, 92, 51), (210, 93, 71), (239, 168, 156), (157, 68, 97), (157, 211, 189), (175, 181, 226), (68, 164, 110), (55, 137, 91), (179, 14, 48), (147, 208, 222), (82, 111, 140), (49, 164, 190), (181, 19, 11)]

#Pattern must be 10 dots by 10 dots (100 dots)
#
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.speed("fast")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots = 100

for dot_count in range(1, number_dots +1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()

#def draw_dot():
for dot in range(10):
    tim.circle(1)
    tim.pencolor(random.choice(colour_list))
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
