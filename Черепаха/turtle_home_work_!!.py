s=input('Enter number:')    
leng=int(input('size:'))

import turtle           
t=turtle.Turtle()
t.shape("turtle")
t.color("purple")
t.shapesize(1)
t.speed(8)
t.penup()
t.backward(300)


def digit(a,b):

    t.penup()
    t.forward(2*l)
    t.pendown()
    for x,k in zip(a,b):
        t.left(k)
        t.fd(x)
    a.reverse()
    b.reverse()
    for x,k in zip(a,b):
        t.backward(x)
        t.right(k)
    t.penup()
    a.reverse()
    b.reverse()    
       

l=leng//2
m=l*2**(0.5)

a0=[l,l,l,l,l,l]
b0=[180,90,0,90,90,0]
a1=[m,m,l,l]
b1=[225,180,225,0]
a2=[l,l,l,m,l]
b2=[180,180,270,315,135]
a3=[l,l,m,l,m]
b3=[180,180,225,135,225]
a4=[l,l,l,l,l]
b4=[270,0,180,90,270]
a5=[l,l,l,l,l]
b5=[180,90,90,270,270]
a6=[m,l,l,l,l]
b6=[225,45,90,90,90]
a7=[l,l,m,l]
b7=[180,180,225,45]
a8=[l,l,l,l,l,l,l,l]
b8=[180,90,90,270,270,270,270,90]
a9=[l,l,l,l,l,m]
b9=[180,90,90,90,180,315]

for i in range(len(s)):
    p=int(s[i])
    
    if p==0:
        digit(a0,b0)
    elif p==1:
        digit(a1,b1)
    elif p==2:
        digit(a2,b2)
    elif p==3:
        digit(a3,b3)
    elif p==4:
        digit(a4,b4) 
    elif p==5:
        digit(a5,b5)
    elif p==6:
        digit(a6,b6)
    elif p==7:
        digit(a7,b7)
    elif p==8:
        digit(a8,b8)
    elif p==9:
        digit(a9,b9)

t.hideturtle()
