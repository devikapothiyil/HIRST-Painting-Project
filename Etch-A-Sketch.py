import turtle

t=turtle.Turtle()
s=turtle.Screen()

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def move_left():
    t.left(10)
    t.forward(10)

def move_right():
    t.right(10)
    t.forward(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(key="w",fun=move_forwards)
s.onkey(key="s",fun=move_backwards)
s.onkey(key="a",fun=move_left)
s.onkey(key="d",fun=move_right)
s.onkey(key="c",fun=clear_screen)

s.exitonclick()
