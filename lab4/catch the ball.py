import pygame, sys, time

import math
from random import randint
from pygame.locals import *


pygame.init()    # установка pygame

FPS = 5
WINDOWHEIGHT = 600
WINDOWWIDTH = 600
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
score = 0
# итератор для обозначения номера шарика
i = 0

# создание переменных направления
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
DIRECTIONS = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]
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

balls = []

def new_ball():
    """
    Function draws a new ball
    :param: x: x coordinate of the center of the ball
    :param: y: x coordinate of the center of the ball
    :param: r: the ball's radius
    :param: color: random color from the list of colors
    :param: direction: random direction from the list of directions
    :return: None
    """
    global x, y, r
    x = randint(100, 500)
    y = randint(100, 500)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    direction = DIRECTIONS[randint(0,3)]
    ball = dict(rect=pygame.Rect(x, y, r, r), color=color, dir=direction, x=x, y=y, rad=r)
    balls.append(ball)

def move_ball():
    """
    Function makes the ball move in a random direction
    :return: None
    """
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


pygame.display.update()    # отображение окна на экране
clock = pygame.time.Clock()
finished = False    # значение по умолчанию - программа продолжается

#user_name = input('Enter user_name: ')    # ввод имени игрока

new_ball()
catched_balls = []
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # если нажата кнопка мыши
            print('Click!')  # печать слова Click в консоли # печать координат текущего мяча
            event.x, event.y = event.pos  # получение координат клика мыши
            for ball in balls:
                if (math.sqrt((event.x - ball['x']) ** 2 + (event.y - ball['y']) ** 2) < ball['rad']):
                    score += 1
                    print('score:', score)
                    print(balls.index(ball))
                    balls.pop(balls.index(ball))
            new_ball()
    screen.fill(BLACK)
    for ball in balls:
        move_ball()
        pygame.draw.ellipse(screen, ball['color'], ball['rect'])
    pygame.display.update()
print('Total score:', score)
pygame.quit()

'''
'# печать общего счета игры в консоль
Total_score = str(score)    # перевод счета из типа int в string
output_score = open('Player table.txt', 'a')    # открытие файла на добавление новых данных
string = [user_name, ' - ', Total_score, ' points', '\n']    # создание строки для вывода в файл
output_score.writelines(string)    # печать строки в файл
output_score.close()    # закрытие файла
'''
#pygame.quit()    # завершение работы pygame
