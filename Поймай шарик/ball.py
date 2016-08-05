import tkinter
from random import choice, randint

ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 50
ball_available_colors = ['red', 'green', 'blue', 'lightgreen', 'purple', 'yellow', 'magenta']


def click_ball(event):
     """ Обработчик событий мышки для игрового холста canvas
     :param event: событие с координатами клика
     По клику мышкой нужно удалять тот объект, на который мышка указывает.
     А также засчитываеть его в очки пользователя.
     """
     event.widget.delete("current")
     # если количество шариков уменьшилось то создаем новый шарик
     if ball_initial_number > len(canvas.find_withtag("oval")):
          create_random_ball()
     # FIXME нужно посчитать количество очков

def move_all_balls(event):
    """ передвигает все шарики на чуть-чуть
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)


def create_random_ball():
    """
    создаёт шарик в случайном месте игрового холста canvas,
     при этом шарик не выходит за границы холста!
    """
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, tag="oval", fill=random_color())


def random_color():
    """
    :return: Случайный цвет из некоторого набора цветов
    """
    return choice(ball_available_colors)


def init_ball_catch_game():
    """
    Создаём необходимое для игры количество шариков, по которым нужно будет кликать.
    """
    for i in range(ball_initial_number):
        create_random_ball()


def init_main_window():
    global root, canvas

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
print("Приходите поиграть ещё!")