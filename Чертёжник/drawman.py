from turtle import Turtle

default_scale = 50

def init_drawman():
    global t, x_current, y_current
    t = Turtle()
    t.speed(50)
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale)

def drawman_scale(scale):
    global dr_scale
    dr_scale = scale

def grid():
    """Координатная сетка.
       Рисуем сеть в зависимости от масштаба - dr_scale.
       После рисования сетки чертежник возвращается в начале координат.
       """

    # Координатная сетка с шагом равным dr_scale
    t.color("gray")
    x = -int(320 / dr_scale)
    y = -int(320 / dr_scale)

    while x <= 320 / dr_scale:
        to_point(x, y)
        pen_down()
        to_point(x, -y)
        pen_up()
        x += 1
    x = -int(320 / dr_scale)
    while y <= 320 / dr_scale:
        to_point(x, y)
        pen_down()
        to_point(-x, y)
        pen_up()
        y += 1

    # Оси координат
    t.pensize(5)
    t.color("black")
    pen_up()
    to_point(-320/dr_scale, 0)
    pen_down()
    to_point(320/dr_scale, 0)
    pen_up()
    to_point(0, -320/dr_scale)
    pen_down()
    to_point(0, 320/dr_scale)
    pen_up()
    t.color("red")
    to_point(0, 0)

def test_drawman():
    """
    Тестирование работы Чертёжника
    :return: None
    """
    to_point(-20, 0)
    pen_down()
    for i in range(5):
        on_vector(10, 15)
        on_vector(0, -15)
    pen_up()
    to_point(0, 0)


def pen_down():
    t.pendown()


def pen_up():
    t.penup()


def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(dr_scale*x_current, dr_scale*y_current)


init_drawman()
if __name__ == '__main__':
    import time

    grid()
    test_drawman()
    time.sleep(2)
