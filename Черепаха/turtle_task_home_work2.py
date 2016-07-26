x = input('Input int number: ')
height = int(input('Input length: ')) # высота цифр

import turtle 

t = turtle.Turtle()
t.shape("turtle")
t.color("red", "yellow")
t.shapesize(2)
t.speed(100)

def main():
    t.penup()
    t.backward(300)

    draw_digit(x)
    t.hideturtle()

def draw_digit(x):
    for i in x:
        if i=='0':
            digit_zero(height)
        elif i=='1':
            digit_one(height)
        elif i=='2':
            digit_two(height)
        elif i=='3':
            digit_three(height)
        elif i=='4':
            digit_four(height)
        elif i=='5':
            digit_five(height)
        elif i=='6':
            digit_six(height)
        elif i=='7':
            digit_seven(height)
        elif i=='8':
            digit_eight(height)
        elif i=='9':
            digit_nine(height)
        t.forward(height/2) 


     

def digit_one(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    t.penup()
    t.forward(height/2)
    t.pendown()
    t.left(90)
    t.forward(height)
    t.left(90+45)
    t.forward(height/2**0.5)
    #обратный ход
    t.backward(height/2**0.5)
    t.right(90+45)
    t.backward(height)
    t.right(90)
    t.penup()

def digit_two(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = height/2
    L2 = (height/2)*2**0.5
    B = [180, -135, 45, 90]
    A = [ L1,   L2, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()
   
def digit_three(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = height/2
    L2 = (height/2)*2**0.5
    B = [45, 135, -135, 135]
    A = [L2, L1,   L2,  L1 ]

    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
        
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()
    t.forward(L1)    

def digit_four(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = height
    L2 = height/2
    B = [90, 180, -90, -90]
    A = [L1, L2,   L2,  L2]

    t.penup()
    t.forward(L2)
    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
        
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()

def digit_five(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L = height/2
    B = [0, 90, 90, -90, -90]
    A = [L, L,  L,   L,   L]

    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
        
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()
    t.forward(L)

def digit_six(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = height/2
    L2 = (height/2)*2**0.5
    B = [90, -90, -90, -90, -90, -45]
    A = [L1,  L1,  L1,  L1,  L1,  L2]

    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
        
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()
    t.forward(L1)    

def digit_seven(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = height/2
    L2 = (height/2)*2**0.5
    B = [90, -45, 135]
    A = [L1,  L2, L1 ]

    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
        
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()
    t.forward(L1)

def digit_eight(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = height
    L2 = height/2
    B = [0,  90, 90, 90, 90, 180, 90]
    A = [L2, L1, L2, L2, L2, L2,  L2]

    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
        
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()
    t.forward(L2)

def digit_nine(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = height/2
    L2 = (height/2)*2**0.5
    B = [45, 45, 90, 90, 90]
    A = [L2, L1, L1, L1, L1]

    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
        
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()
    t.forward(L1)    

def digit_zero(height):
    """ Рисует цифру с высотой height
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    L1 = height
    L2 = height/2
    B = [0,  90, 90, 90]
    A = [L2, L1, L2, L1]

    t.pendown()
    for height, degree in zip(A, B):
        t.left(degree)
        t.forward(height)
        
    A.reverse()
    B.reverse()
    for height, degree in zip(A, B):
        t.backward(height)
        t.right(degree)
    t.penup()
    t.forward(L2)
    

#input("? Int x = ",x)
main()



#t.left(30)
#t.right(30)
#t.forward(200)
#t.backward(200)
#t.penup()
#t.pendown()
#t.begin_fill()
#t.end_fill()
