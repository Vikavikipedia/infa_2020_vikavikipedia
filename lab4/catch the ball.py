import random
import pygame
import math

from random import randint
from pygame.locals import *

pygame.init()

FPS = 10
WINDOWHEIGHT = 600
WINDOWWIDTH = 600
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
# Initial count value
score = 0

DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
UP = 'top'
DOWN = 'bottom'
LEFT = 'left'
RIGHT = 'right'
DIRECTIONS = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]
VECTOR = [UP, DOWN, LEFT, RIGHT]
MOVESPEED = 1

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

balls = []
cubes = []

def new_ball():
    """
    Function draws a new ball and appends it to the list of balls
    x: x coordinate of the center of the ball
    y: y coordinate of the center of the ball
    r: the ball's radius
    color: random color from the list of colors
    direction: random direction from the list of directions
    :return: None
    """
    global x, y, r
    x = randint(100, 500)
    y = randint(100, 500)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    direction = DIRECTIONS[randint(0,3)]
    ball = dict(rect=pygame.Rect(x, y, r, r), color=color, dir=direction)
    balls.append(ball)

def new_cube():
    """
    Function draws a new cube and appends it to the list of cubes
    a: x coordinate of the left bottom corner of the cube
    b: y coordinate of the left bottom corner of the cube
    w: full width of the cube
    h: full height of the cube
    color: random color from the list of colors
    direction: random direction from the list of directions
    :return: None
    """
    global a, b, w, h
    a = randint(100, 500)
    b = randint(100, 500)
    w = randint(10, 100)
    h = randint(10, 100)
    cube_color = COLORS[randint(0, 5)]
    vector = VECTOR[randint(0,3)]
    cube = dict(rect=pygame.Rect(a, b, w, h), color=cube_color, dir=vector)
    cubes.append(cube)

def move_ball():
    """
    Function makes the ball move. The ball bounces off the wall when it hits it
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

def move_cube():
    """
    Function makes the cube move. The cube bounces off the wall when it hits it
    :return: None
    """
    if cube['dir'] == DOWN:
            cube['rect'].top += 2 * MOVESPEED
    if cube['dir'] == UP:
            cube['rect'].top -= 2 * MOVESPEED
    if cube['dir'] == LEFT:
            cube['rect'].left -= 2*MOVESPEED
    if cube['dir'] == RIGHT:
            cube['rect'].left += 2*MOVESPEED
    if cube['rect'].top < 0:
        cube['dir'] = DOWN
    if cube['rect'].bottom > WINDOWHEIGHT:
        cube['dir'] = UP
    if cube['rect'].left < 0:
        cube['dir'] = RIGHT
    if cube['rect'].right > WINDOWWIDTH:
        cube['dir'] = LEFT


def cube_move_like_a_snake():
    """
    This function makes a rectangle move like a snake, randomly turning at right angle.
    New direction depends on a vector_choise
    :return: None
    """
    vector_choise = random.randint(0, 20)
    if cube['dir'] == DOWN and vector_choise == 0:
            cube['dir'] = VECTOR[randint(0,3)]
    if cube['dir'] == UP and vector_choise == 0:
            cube['dir'] = VECTOR[randint(0,3)]
    if cube['dir'] == LEFT and vector_choise == 0:
            cube['dir'] = VECTOR[randint(0,3)]
    if cube['dir'] == RIGHT and vector_choise == 0:
            cube['dir'] = VECTOR[randint(0,3)]


pygame.display.update()
clock = pygame.time.Clock()
finished = False

user_name = input('Enter user_name: ')

new_ball()
new_cube()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:  # если нажата кнопка мыши
            print('Click!')  # печать слова Click в консоли # печать координат текущего мяча
            event.x, event.y = event.pos  # получение координат клика мыши
            for ball in balls:
                #click_ball()
                if math.sqrt((event.x - (ball['rect'].centerx)) ** 2 +
                              (event.y - ball['rect'].centery) ** 2) < 0.5 * ball['rect'].width:
                    score += 1
                    print('+1')
                    balls.pop(balls.index(ball))
            for cube in cubes:
                if cube['rect'].collidepoint(event.pos):
                    score += 5
                    print('+5')
#                   print(cube)
                    cubes.pop(cubes.index(cube))
            shape_choise = random.randint(0,1)
            if shape_choise == 0:
                new_cube()
            else:
                new_ball()
    screen.fill(BLACK)
    for ball in balls:
        move_ball()
        pygame.draw.ellipse(screen, ball['color'], ball['rect'])
    for cube in cubes:
        cube['rect'].inflate_ip(-1, -1)
        cube_move_like_a_snake()
        move_cube()
        pygame.draw.rect(screen, cube['color'], cube['rect'])
    pygame.display.update()

print('Total score:', score)
Total_score = str(score)
output_score = open('Player table.txt', 'a')
string = [user_name, ' - ', Total_score, ' points', '\n']
output_score.writelines(string)
output_score.close()
pygame.quit()
