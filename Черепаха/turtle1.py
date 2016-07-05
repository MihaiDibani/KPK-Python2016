from turtle import *
t = Turtle()
t.shape("turtle")
t.shapesize(2)
t.color("red", "yellow")

t.begin_fill()

for i in range(5):
    for k in range(3):
        t.forward(100)
        t.left(360/3)
        
    t.forward(100)
    t.right(360/5)

    
t.end_fill()

#t.begin_fill()
#t.end_fill()
    
#t.left(30)
#t.right(30)
#t.forward(100)
#t.backward(200)
#t.penup()
#t.pendown()


