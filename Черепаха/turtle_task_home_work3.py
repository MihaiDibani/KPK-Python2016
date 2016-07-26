import turtle
from math import sin

screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen","yellow")
t.shapesize(1)
t.speed(1)
t.penup()
t.backward(200)

def draw_number(n,length = 100):
     """ Рисует цифру с высотой 100 слева от направления черепашки
            контракт (договорённость):
                черепаха останавливается в следующей стартовой  точке
                имеет исходную ориентацию
                перо оказывается поднятым по окончании функции
        """
     L1 = length/2
     L2 = (length/2)*2**0.5
     if n == 1:
         B = [90, -45, -135, 90] # угол поворота
         A = [L1, L2, 2*L1,  0]  # расстояние
         C = [0, 1, 1, 0]        # контроль пера 0-поднять, 1-опустить
        
     elif n == 2:
        B = [90,   -90, -90, -45, 135]
        A = [ 2*L1, L1,  L1, L2,  L1]
        C = [0,     1,   1,  1,    1]
        
     elif n == 3:
        B = [45,   135, -135, 135, 180, -90, 90]
        A = [ L2,  L1,  L2,    L1,  L1, 2*L1, 0]
        C = [1,     1,   1,     1,    0,  0, 0]

     elif n == 4:
        B = [90,   180,  90, 90, 180, 90]
        A = [ 2*L1,  L1,  L1, L1,  2*L1,0]
        C = [0,     1,    1,  1,    1, 0]

     elif n == 5:
        B = [0,   90,  90, -90, -90, -90, 90]
        A = [L1,  L1,  L1,  L1,  L1, 2*L1, 0]
        C = [1,    1,   1,   1,   1,  0,   0]    

     elif n == 6:
        B = [0,   90,  90, -135, 180, 45, 90]
        A = [L1,  L1,  L1,  L2,  L2,  L1, L1]
        C = [1,    1,   1,   1,   1,  1,   1]

     elif n == 7:
        B = [90,   -45,  135, 180, -90, 90]
        A = [L1,  L2,    L1,  L1,  2*L1, 0]
        C = [1,    1,    1,   0,   0,    0]
        
     elif n == 0:
        B = [0,   90,   90,  90,  90]
        A = [L1,  2*L1,  L1, 2*L1,  L1]
        C = [1,    1,    1,   1,   1]
        
     elif n == 8:
        B = [0,   90,  90,  180,  90,  90, 90, 90]
        A = [L1,  L1,  L1,  L1,   L1,  L1,2*L1, L1]
        C = [1,    1,    1,   1,   1,   1,  1 , 1]
        
     elif n == 9:
        B = [45,   45,  90, 90, 90, -90, 90]
        A = [L2,  L1,  L1,  L1,  L1,  L1, 0]
        C = [1,    1,   1,   1,   1,  0, 0]
        
     for lenght, degree, pen in zip(A, B, C):
        if pen == 1:
            t.pendown()
        else:
            t.penup()
        t.left(degree)
        t.forward(lenght)     
     t.penup()
     t.forward(L1)     
        
A=input()
for i in range(len(A)):
    draw_number(int(A[i]),100)
