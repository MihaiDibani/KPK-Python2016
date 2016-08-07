from tkinter import *
from random import choice, randint
from tkinter import messagebox
from math import sqrt

screen_width = 500
screen_height = 350
timer_delay = 50
best_scores = 1000000
shoots = 0

class Ball:
    initial_number = 20
    minimal_radius = 15
    maximal_radius = 40
    available_colors = ['red', 'green', 'blue', 'orange', 'magenta', 'lightgray']

    def __init__(self):
        """
        создаёт шарик в случайном месте игрового холста canvas,
        при этом шарик не выходит за границы холста!
        """
        R = randint(Ball.minimal_radius, Ball.maximal_radius)
        x = randint(0, screen_width-1-2*R)
        y = randint(0, screen_height-1-2*R)
        self._R = R
        self._x = x
        self._y = y
        fillcolor = choice(Ball.available_colors)
        self._avatar = canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=fillcolor, outline=fillcolor)
        self._Vx = randint(-1, +1)
        self._Vy = randint(-1, +1)

    def explode(self):
        canvas.delete(self._avatar)
        if self in shells_on_fly:
            shells_on_fly.remove(self)
        if self in balls:
            balls.remove(self)

    def fly(self):
        self._x += self._Vx
        self._y += self._Vy
        if self in balls: # если объект - шарик то отразить его от стен
            if self._x < 2:
                self._x = 2
                self._Vx = -self._Vx
            elif self._x + 2 * self._R >= screen_width:
                self._x = screen_width - 2 * self._R - 1
                self._Vx = -self._Vx
            if self._y < 3:
                self._y = 3
                self._Vy = -self._Vy
            elif self._y + 2 * self._R >= screen_height:
                self._y = screen_height - 2 * self._R - 1
                self._Vy = -self._Vy
        elif self in shells_on_fly: # если объект снаряд то:
            # если снаряд больше половины выходит за стены то он взрывается
            if (self._x + self._R < 0) or (self._x >= screen_width - self._R ) or (self._y < 0) or (self._y >= screen_height - self._R):
                self.explode()
        canvas.coords(self._avatar, self._x, self._y, self._x + 2 * self._R, self._y + 2 * self._R)

class Gun:
    def __init__(self):
        self._x = 0
        self._y = screen_height - 1
        self._lx = 30
        self._ly = -30
        self._length = sqrt(self._lx * self._lx + self._ly * self._ly)
        self._avatar = canvas.create_line(self._x, self._y, self._x+self._lx, self._y+self._ly, width=10)
    def shoot(self):
        """
        :return: объект снаряда
        """
        shell = Ball()
        shell._R = 5
        shell._x = self._x + self._lx - shell._R
        shell._y = self._y + self._ly - shell._R
        shell._Vx = self._lx/10
        shell._Vy = self._ly/10
        shell.fly()
        return shell

def move_gun_event(event):
    """
    Пушка двигается в направлении курсора
    :param event:
    :return:
    """
    global gun, canvas
    k = sqrt(event.x**2 + (screen_height - event.y)**2) / gun._length
    gun._lx = event.x/k
    gun._ly = -(screen_height-event.y)/k
    canvas.coords(gun._avatar, 0, screen_height, gun._lx, screen_height+gun._ly)


def timer_event():
    global scores_value, scores_text, number_of_shots, shoots, best_scores, gun

    # проверяем на столкновение снаряда с каждым шариком
    for shell in shells_on_fly:
        for ball in balls:
            # d1 - расстояние между центром снаряда и шарика
            d1 = sqrt((shell._x + shell._R - ball._x - ball._R)**2 + (shell._y + shell._R - ball._y - ball._R)**2)
            d2 = shell._R + ball._R
            if d1 <= d2:
                ball.explode()
                shell.explode()
                scores_value.set(scores_value.get()-1)
    scores_text["textvariable"]=scores_value
    number_of_shots["text"] = 'Выстрелов: '+str(shoots)

    if scores_value.get() == 0:
        scores_value.set(Ball.initial_number)
        if best_scores > shoots:
            best_scores = shoots
        canvas.delete(gun._avatar)
        if messagebox.askokcancel("Итоги игры", 'Потрачено снарядов:'+str(shoots)+'\nЛучший результат:'+str(best_scores)+'\nСыграем ещё?'):
            reset_game()
        else:
            root.destroy()

    for ball in balls:
        ball.fly()
    for shell in shells_on_fly:
        shell.fly()

    canvas.after(timer_delay, timer_event)


def click_event_handler(event):
    global shells_on_fly, gun, shoots
    shell = gun.shoot()
    shells_on_fly.append(shell)
    shoots += 1


def init_main_window():
    global root, canvas, scores_text, number_of_shots, scores_value, shoots
    root = Tk()
    root.title("Пушка")
    scores_value = IntVar()
    scores_value.set(Ball.initial_number)
    canvas = Canvas(root, background='white', width=screen_width, height=screen_height)
    scores_text = Label(root, textvariable=scores_value)
    number_of_shots = Label(root, text='Выстрелов: '+str(shoots))
    canvas.grid(row=1, column=0, columnspan=3)
    scores_text.grid(row=0, column=2)
    number_of_shots.grid(row=0,column=1)
    canvas.bind('<Button-1>', click_event_handler)


def init_game():
    """
    Создаём необходимое для игры количество объектов-шариков,
    а также объект - пушку.
    """
    global balls, gun, shells_on_fly, shoots
    balls = []
    balls = [Ball() for i in range(Ball.initial_number)]
    gun = Gun()
    shells_on_fly = []
    shoots = 0 # количество выстрелов
    canvas.bind('<Motion>', move_gun_event)


def reset_game():
    init_game()
    timer_event()


if __name__ == "__main__":
    init_main_window()
    init_game()
    timer_event()
    root.mainloop()