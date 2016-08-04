from tkinter import *


def button1_command():
    print('Button 1 default command.')


def print_hello(event):
    #print('char=',event.char)
    #print('keycode=',event.keycode)
    print('num=',event.num)
    print('x, y=',event.x, event.y)
    #print('x_root, y_root =',event.x_root, event.y_root)
    me = event.widget
    if me == button1:
        print('You pressd button1!')
    elif me == button2:
        print('You pressed button2!')
    else:
        raise ValueError()


root = Tk() # создаем виджет главного окна

button1 = Button(root, text="Button1", command=button1_command)
button1.bind("<Button>", print_hello)
button1.pack()                           # запаковка виджета

button2 = Button(root, text="Button2")  # создание виджета кнопки
button2.bind("<Button>", print_hello)  # привязка события к кнопке button
button2.pack()

root.mainloop()#цикл ожидания событий