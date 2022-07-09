import pygame

from pygame.draw import *

pygame.init()

FPS = 1
screen = pygame.display.set_mode((400, 400))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

screen.fill(BLACK)
circle(screen, GREEN, (200, 200), 20)

one_ball = circle(screen, GREEN, (200, 200), 20)
moving_ball = (one_ball, 'upright')

pygame.display.update()    # отображение окна на экране
clock = pygame.time.Clock()
finished = False

while not finished:    # запуск игрового цикла
    clock.tick(FPS)
    for event in pygame.event.get():    # проверка всех происходящих событий
        if event.type == pygame.QUIT:    # если нажата кнопка закрытия окна, то выход
            finished = True
        else:
            if moving_ball[0] == 'downleft':
                moving_ball[1].left -= MOVESPEED
                moving_ball[0].top += MOVESPEED
            if moving_ball[1] == 'downright':
                moving_ball[0].left += MOVESPEED
                moving_ball[1].top += MOVESPEED
            if moving_ball[0] == 'upleft':
                moving_ball[1].left -= MOVESPEED
                moving_ball[1].top -= MOVESPEED
            if moving_ball[0] == 'upright':
                moving_ball[1].left += MOVESPEED
                moving_ball[1].top -= MOVESPEED

pygame.quit()

