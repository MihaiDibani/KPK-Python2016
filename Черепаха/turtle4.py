from turtle import *
t = Turtle()
t.shape("turtle")
t.shapesize(2)
t.color("red", "yellow")

t.penup()
t.backward(200)

for i in range(20):
    t.pendown()
    t.forward(i)
    t.penup()
    t.forward(i)

    

t.hideturtle()


#t.begin_fill()
#t.end_fill()
    
#t.left(30)
#t.right(30)
#t.forward(100)
#t.backward(200)
#t.penup()
#t.pendown()


