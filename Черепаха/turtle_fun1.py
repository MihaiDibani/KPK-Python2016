from turtle import *
t = Turtle()
t.shape("turtle")
t.shapesize(2)
t.color("red", "yellow")

def triangle(length):
    """ Рисует треугольник с ребром length
        слева от направления черепашки.

        Черепашка возвращается в исходную точку.
        После рисования перо поднимается."""
    t.pendown()
    for k in range(3):
        t.forward(length)
        t.left(360/3)
    t.penup()

t.penup()
t.backward(300)
for i in range(6):
    triangle(50)
    t.forward(100)
    

t.hideturtle()     


#t.begin_fill()
#t.end_fill()
    
#t.left(30)
#t.right(30)
#t.forward(100)
#t.backward(200)
#t.penup()
#t.pendown()


