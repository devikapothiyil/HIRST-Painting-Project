import turtle
import random

t=turtle.Turtle()
no_of_sides=3
color_list=["red","green","yellow","blue","orange","black","pink","aquamarine","DeepSkyBlue"]
while no_of_sides != 11:
    my_color = random.choice(color_list)
    t.pencolor(my_color)
    for _ in range(no_of_sides):
        angle = 360 / no_of_sides
        t.forward(100)
        t.left(angle)
    no_of_sides+=1

scn=turtle.Screen()
scn.exitonclick()
