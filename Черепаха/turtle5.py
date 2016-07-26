from turtle import *
t = Turtle()
t.shape("turtle")
t.shapesize(2)
t.color("red", "yellow")
t.speed(10)

t.penup()
t.backward(100)

A = [30, 20, 30, 50, 10, 20]
B = [60, 30, 30, 90, 90, 60]

t.pendown()

for length, degree in zip(A, B):
    t.left(degree)
    t.forward(length)


t.hideturtle()     


#t.begin_fill()
#t.end_fill()
#t.speed(10)    
#t.left(30)
#t.right(30)
#t.forward(100)
#t.backward(200)
#t.penup()
#t.pendown()


