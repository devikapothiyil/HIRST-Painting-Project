# import colorgram
#
# colors = colorgram.extract('hirst.jpg', 30)
# rgb_list=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_list.append(new_color)
#
# print(rgb_list)

import random
import turtle
turtle.colormode(255)

t=turtle.Turtle()
t.hideturtle()
color_list=[(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71),
            (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229),
            (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
            (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

t.penup()
x=0
y=-70
t.goto(x,y)
t.pendown()
while y != 500:
    for i in range(10):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.forward(50)
        t.pendown()
    x=0
    y+=50
    t.penup()
    t.goto(x,y)
    t.pendown()

scan=turtle.Screen()
scan.exitonclick()
