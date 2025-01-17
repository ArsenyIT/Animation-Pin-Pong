# 1. Импор Библиотек
from tkinter import *
import time
import random

# 3. Класс Ball, должен двигатся, должен появится, Видел границы
class Ball():
    def __init__(self, canvas, color, platform1, platform2):
        self.platform1 = platform1
        self.platform2 = platform2
        self.canvas = canvas
        self.speed = 6
        self.shet1 = 0
        self.shet2 = 0
        self.oval = canvas.create_oval(200, 100, 230, 130, fill=color)
        self.x = self.speed
        self.y = self.speed
        self.text1 = self.canvas.create_text(100, 20, font='Arial 15', text=f'Счёт: {self.shet1}')
        self.text2 = self.canvas.create_text(400, 20, font='Arial 15', text=f'Счёт: {self.shet2}')

    def game_over1(self):
        self.canvas.moveto(self.text1, 210, 200)
        self.canvas.itemconfigure(self.text1, font='Arial 20', text=f'Выйграл 1 Игрок', fill='red')
        self.canvas.moveto(self.oval, 10, -7)
        self.speed = 0

    def game_over2(self):
        self.canvas.moveto(self.text2, 210, 200)
        self.canvas.itemconfigure(self.text2, font='Arial 20', text=f'Выйграл 2 Игрок', fill='red')
        self.canvas.moveto(self.oval, 10, -7)
        self.speed = 0

    def touch_platform1(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform1.rect1)
        if ball_pos[2] <= platform_pos[2] and ball_pos[2] >= platform_pos[0]:
            if ball_pos[1] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True

    def touch_platform2(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform2.rect2)
        if ball_pos[0] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[1] >= platform_pos[1] and ball_pos[3] <= platform_pos[3]:
                return True

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        pos = self.canvas.coords(self.oval)
        if pos[1] <= 0:
            self.y = self.speed
        if pos[3] >= 400:
            self.speed = 6
            self.y = -self.speed
        if pos[0] <= 0:
            self.shet2 += 1
            if self.shet2 >= 10:
                self.game_over2()
            else:
                self.canvas.itemconfigure(self.text2, text=f'Счёт: {self.shet2}')
            self.x = self.speed
        if pos[2] >= 500:
            self.shet1 += 1
            if self.shet1 >= 10:
                self.game_over1()
            else:
                self.canvas.itemconfigure(self.text1, text=f'Счёт: {self.shet1}')
            self.x = -self.speed
        if self.touch_platform1(pos) == True:
            self.x *= -1
        if self.touch_platform2(pos) == True:
            self.x *= -1
# 8. Родительский класс
class Platform():
    def up(self, event):
        pass

    def down(self, event):
        pass

    def draw(self):
        pass

# 4. Класс Платформ1, описать платформу, научится двигатся
class Platform1(Platform):
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect1 = canvas.create_rectangle(490, 150, 500, 250, fill=color)
        self.y = 0
        self.canvas.bind_all('<KeyPress-Up>', self.up)
        self.canvas.bind_all('<KeyPress-Down>', self.down)

    def up(self, event):
        self.y = -9

    def down(self, event):
        self.y = 9

    def draw(self):
        self.canvas.move(self.rect1, 0, self.y)
        pos = self.canvas.coords(self.rect1)
        if pos[1] <= 0:
            self.canvas.moveto(self.rect1, 490, 0)
        if pos[3] >= 400:
            self.canvas.moveto(self.rect1, 490, 300)

# 5. Класс Платформ2, описать платформу, научится двигатся
class Platform2(Platform):
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect2 = canvas.create_rectangle(0, 150, 10, 250, fill=color)
        self.y = 0
        self.canvas.bind_all('<KeyPress-w>', self.w)
        self.canvas.bind_all('<KeyPress-s>', self.s)

    def w(self, event):
        self.y = -9

    def s(self, event):
        self.y = 9

    def draw(self):
        self.canvas.move(self.rect2, 0, self.y)
        pos = self.canvas.coords(self.rect2)
        if pos[1] <= 0:
            self.canvas.moveto(self.rect2, 0, 0)
        if pos[3] >= 400:
            self.canvas.moveto(self.rect2, 0, 300)

# 2. Cоздать окно
window = Tk()
window.title('Аркада')
window.resizable(0, 0)
canvas = Canvas(window, w=500, height=400, bg='lightgrey')
canvas.pack()
# 6. Создать объекты
pole_image = PhotoImage(file='Новый проект.png')
pole = canvas.create_image(0, 0, image=pole_image, anchor=NW)
platform1 = Platform1(canvas, 'blue')
platform2 = Platform2(canvas, 'blue')
ball = Ball(canvas, 'red', platform1, platform2)
# 7. Игровой цикл
while True:
    ball.draw()
    platform1.draw()
    platform2.draw()
    time.sleep(0.02)
    window.update()

window.mainloop()