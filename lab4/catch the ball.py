import pygame
import math

from pygame.draw import *
from random import randint

pygame.init()

FPS = 1
screen = pygame.display.set_mode((800, 800))

score = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """
    Function draws a new ball
    :param: x: x coordinate of the center of the ball
    :param: y: x coordinate of the center of the ball
    :param: r: the ball's radius
    :param: color: random color from the list of colors
    :return: None
    """
    global x, y, r
    x = randint(100, 900)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    """
    Function prints coordinates and radius of current circle
    :return: None
    """
    print(x, y, r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

user_name = input('Enter user_name: ')

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)
            event.x, event.y = event.pos
            if math.sqrt((event.x - x) ** 2 + (event.y - y) ** 2) < r:
                score += 1
                print('score:', score)

    new_ball()
    pygame.display.update()
    screen.fill(BLACK)
print('Total score:', score)
Total_score = str(score)
output_score = open('Player table.txt', 'a')
string = [user_name, ' - ', Total_score, ' points', '\n']
output_score.writelines(string)
output_score.close()

pygame.quit()
