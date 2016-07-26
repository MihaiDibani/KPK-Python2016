from drawman import *
from time import sleep

drawman_scale(50)   # указываем масштаб

grid()              # рисуем координатную сетку

def f(x):
    return x*x

x  = -4.0
to_point(x, f(x))
pen_down()
while x < 4:
    to_point(x, f(x))
    x += 0.1
pen_up()

sleep(5)            # ждем 5 секунд