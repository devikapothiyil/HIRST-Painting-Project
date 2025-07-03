import random
import turtle

s=turtle.Screen()
s.setup(width=500,height=400)
userguess=s.textinput(title="Make a bet",prompt="Which turtle will win the race:")
x=-100
y=-100
colorlist=["red","green","blue","yellow","violet","orange"]

all_turtles=[]
for turtles in range(6):
    new_turtle=turtle.Turtle("turtle")
    new_turtle.color(colorlist[turtles])
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y+=50

if userguess:
    race_mode="on"

while race_mode=="on":
    for turt in all_turtles:
        if turt.xcor() > 230:
            race_mode="off"
            winning_color=turt.pencolor()
            if userguess== winning_color:
                print(f"You win!!{winning_color} is the won turtle")
            else:
                print(f"You lose!!{winning_color} is the won turtle")
        random_dist=random.randint(0,10)
        turt.forward(random_dist)
