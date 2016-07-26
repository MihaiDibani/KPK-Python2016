import turtle
from math import sqrt

t = turtle.Turtle()           # Начальные установки. Инициализация Черепашки и холста...
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(1)
t.speed(10)
t.penup() 
t.back(300)
t.pensize(3)

def digit_all(cif,length): # Контракт с черепахой проходить весь путь маски - все 9 сегментов
                           # Черепашку уговорил только после того, что она будет круче трамвая,
                           # бегая по одному и тому же пути. Черепашка радовалась, что заменив
                           # только путь можно изменить все цифры сразу.
    if cif==0:
        A=[1,2,3,7,8,9]    # списки сегментов матрицы цифр 0-9 для Черепашки, чтобы ведала. какой прочерчивать.   
    if cif==1:
        A=[4,8,9]          #   нумерация сегментов. Черепашка двигается снизу-слева и добегает в правый-верхний угол без отрыва.
    if cif==2:                #             
        A=[3,6,7,9]           #        3
    if cif==3:                #    2   4   9
        A=[3,4,5,6]           #        5 
    if cif==4:                #    1   6   8
        A=[2,5,8,9]           #        7    
    if cif==5:                #
        A=[2,3,5,7,8]
    if cif==6:
        A=[1,2,3,5,7,8]
    if cif==7:
        A=[1,3,4]
    if cif==8:
        A=[1,2,3,5,7,8,9]        
    if cif==9:
        A=[2,3,5,7,8,9]      
    t.penup()    
    t.left(90)
    if 1 in A:              # пробегаем все 9 сегментов. Если сегмент есть в списке - опускаем перо и рисуем
        t.pendown()
    t.forward(length/2)
    t.penup()
    if 2 in A:
        t.pendown()
    t.forward(length/2)
    t.right(90)
    t.penup()    
    if 3 in A:
        t.pendown()
    t.forward(length/2)
    t.right(90+45)
    t.penup()
    if 4 in A:
        t.pendown()
    t.forward(length/2*sqrt(2))
    t.left(90+45)
    t.penup()
    if 5 in A:
        t.pendown()
    t.forward(length/2)
    t.right(90+45)
    t.penup()    
    if 6 in A:
        t.pendown()
    t.forward(length/2*sqrt(2))
    t.left(90+45)
    t.penup()    
    if 7 in A:
        t.pendown()
    t.forward(length/2)
    t.left(90)
    t.penup()    
    if 8 in A:
        t.pendown()
    t.forward(length/2)
    t.penup()    
    if 9 in A:                         # пробежали все 9 сегментов. Черепашке тяжело, но сделали универсальную функцию
        t.pendown()
    t.forward(length/2)
    t.penup()
    t.left(180)
    t.forward(length)
    t.left(90)
    t.forward(length/2)

def draw_num(x):                       # поступил проще - загнал число в строку и по символам обрабатывал
    x_str = str(x)
    for symb in x_str:
        dig = int(symb)
        digit_all(dig,60)
                  
        
draw_num(21485060379)                      # вызов главной процедуры печати числа. Черепашка довольна.
