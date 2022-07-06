import pygame, sys, time

from pygame.draw import *
from random import randint
from pygame.locals import *


pygame.init()    # установка pygame

FPS = 1
WINDOWHEIGHT = 600
WINDOWWIDTH = 600
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
score = 0

# создание переменных направления
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
# скорость движения
MOVESPEED = 3
# назначение цветов
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
# создается список цветов
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_balls():
    """
    Function draws a new ball
    :param: x: x coordinate of the center of the ball
    :param: y: x coordinate of the center of the ball
    :param: r: the ball's radius
    :param: color: random color from the list of colors
    :return: None
    """
    global x_1, x_2, x_3, y_1, y_2, y_3, r_1, r_2, r_3
    x_1 = randint(100, 700)
    y_1 = randint(100, 700)
    r_1 = randint(10, 100)
    color_1 = COLORS[randint(0, 5)]
    ball_1 = dict(circle=circle(screen, color_1, (x_1, y_1), r_1),color=color_1, dir=UPRIGHT)
    x_2 = randint(100, 700)
    y_2 = randint(100, 700)
    r_2 = randint(10, 100)
    color_2 = COLORS[randint(0, 5)]
    ball_2 = dict(circle=circle(screen, color_2, (x_2, y_2), r_2),color=color_2, dir=UPLEFT)
    x_3 = randint(100, 700)
    y_3 = randint(100, 700)
    r_3 = randint(10, 100)
    color_3 = COLORS[randint(0, 5)]
    ball_3 = dict(circle=circle(screen, color_3, (x_3, y_3), r_3),color=color_3, dir=DOWNLEFT)


def move_ball():
    """
    Function makes the ball move in a random direction
    :return: None
    """


def click(event):
    """
    Function prints coordinates and radius of current circle
    :return: None
    """
    print(x, y, r)


pygame.display.update()    # отображение окна на экране
clock = pygame.time.Clock()
finished = False    # значение по умолчанию - программа продолжается

#user_name = input('Enter user_name: ')    # ввод имени игрока

x_1 = randint(100, 500)
y_1 = randint(100, 500)
r_1 = randint(10, 100)
color_1 = COLORS[randint(0, 5)]
ball_1 = dict(rect=pygame.Rect(x_1, y_1, r_1, r_1), color=color_1, dir=UPRIGHT, x=x_1, y=y_1, rad=r_1)
x_2 = randint(100, 500)
y_2 = randint(100, 500)
r_2 = randint(10, 100)
color_2 = COLORS[randint(0, 5)]
ball_2 = dict(rect=pygame.Rect(x_2, y_2, r_2, r_2), color=color_2, dir=UPLEFT, x=x_2, y=y_2, rad=r_2)
x_3 = randint(100, 500)
y_3 = randint(100, 500)
r_3 = randint(10, 100)
color_3 = COLORS[randint(0, 5)]
ball_3 = dict(rect=pygame.Rect(x_3, y_3, r_3, r_3), color=color_3, dir=DOWNLEFT, x=x_3, y=y_3, rad=r_3)

balls = [ball_1, ball_2, ball_3]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    for ball in balls:
        if ball['dir'] == DOWNLEFT:
            ball['rect'].left -= MOVESPEED
            ball['rect'].top += MOVESPEED
        if ball['dir'] == DOWNRIGHT:
            ball['rect'].left += MOVESPEED
            ball['rect'].top += MOVESPEED
        if ball['dir'] == UPLEFT:
            ball['rect'].left -= MOVESPEED
            ball['rect'].top -= MOVESPEED
        if ball['dir'] == UPRIGHT:
            ball['rect'].left += MOVESPEED
            ball['rect'].top -= MOVESPEED
        if ball['rect'].top < 0:
            if ball['dir'] == UPLEFT:
                ball['dir'] = DOWNLEFT
            if ball['dir'] == UPRIGHT:
                ball['dir'] = DOWNRIGHT
        if ball['rect'].bottom > WINDOWHEIGHT:
            if ball['dir'] == DOWNLEFT:
                ball['dir'] = UPLEFT
            if ball['dir'] == DOWNRIGHT:
                ball['dir'] = UPRIGHT
        if ball['rect'].left < 0:
            if ball['dir'] == DOWNLEFT:
                ball['dir'] = DOWNRIGHT
            if ball['dir'] == UPLEFT:
                ball['dir'] = UPRIGHT
        if ball['rect'].right > WINDOWWIDTH:
            if ball['dir'] == DOWNRIGHT:
                ball['dir'] = DOWNLEFT
            if ball['dir'] == UPRIGHT:
                ball['dir'] = UPLEFT
        pygame.draw.ellipse(screen, ball['color'], ball['rect'])
    pygame.display.update()
    time.sleep(0.02)

'''    
        elif event.type == pygame.MOUSEBUTTONDOWN:     # если нажата кнопка мыши
            print('Click!')    # печать слова Click в консоли
            click(event)    # печать координат текущего мяча
            event.x, event.y = event.pos    # получение координат клика мыши
            if (math.sqrt((event.x - x_1) ** 2 + (event.y - y_1) ** 2) < r_1
                or math.sqrt((event.x - x_2) ** 2 + (event.y - y_2) ** 2) < r_2
                or math.sqrt((event.x - x_3) ** 2 + (event.y - y_3) ** 2) < r_3):    # если клик мыщи попал в мяч
                score += 1    # увеличение счета на 1 и печать текущего счета в консоли
                print('score:', score)

    #new_balls()
#рисование нового мяча
pygame.display.update()     # отображение окна на экране
# Заливка экрана черным для удаления прерыдущего шарика
screen.fill(BLACK)

print('Total score:', score)    # печать общего счета игры в консоль
Total_score = str(score)    # перевод счета из типа int в string
output_score = open('Player table.txt', 'a')    # открытие файла на добавление новых данных
string = [user_name, ' - ', Total_score, ' points', '\n']    # создание строки для вывода в файл
output_score.writelines(string)    # печать строки в файл
output_score.close()    # закрытие файла
'''
#pygame.quit()    # завершение работы pygame
