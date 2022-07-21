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


class Balloon:
    random_x = randint(100, 500)
    random_y = randint(100, 500)
    random_radius = randint(10, 100)
    random_color = COLORS[randint(0, 5)]
    random_direction = DIRECTIONS[randint(0, 3)]

    def __init__(self):
        self.x, self.y = Balloon.random_x, Balloon.random_y
        self.radius = Balloon.random_radius
        self.color = Balloon.random_color
        self.direction = Balloon.random_direction
        self.one_balloon = dict(rect=pygame.Rect(self.x, self.y, self.radius, self.radius),
                                color=self.color, dir=self.direction)

    def appear(self, list_of_balloons):
        pygame.draw.ellipse(screen, self.one_balloon['color'], self.one_balloon['rect'])
        list_of_balloons.append(self.one_balloon)

    def reflect(self):
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

    def click(self, click_position, score):
        event_x, event_y = click_position  # получение координат клика мыши
        for ball in balls:
            if math.sqrt((event_x - ball['rect'].centerx) ** 2 +
                         (event_y - ball['rect'].centery) ** 2) < 0.5 * ball['rect'].width:
                score += 1
                print('+1')
                balls.pop(balls.index(ball))


class Cube:
    random_x = randint(100, 500)
    random_y = randint(100, 500)
    random_weight = randint(10, 100)
    random_height = randint(10, 100)
    random_color = COLORS[randint(0, 5)]
    random_vector = VECTOR[randint(0, 3)]
    vector_choise = random.randint(0, 20)

    def __init__(self):
        self.x, self.y = Cube.random_x, Cube.random_y
        self.w, self.h = Cube.random_weight, Cube.random_height
        self.color = Cube.random_color
        self.vector = Cube.random_vector
        self.one_cube = dict(rect=pygame.Rect(self.x, self.y, self.w, self.h),
                             color=self.color, dir=self.vector)

    def appear(self):
        pygame.draw.rect(screen, self.one_cube['color'], self.one_cube['rect'])

    def reflect(self):
        if cube['dir'] == DOWN:
            cube['rect'].top += 2 * MOVESPEED
        if cube['dir'] == UP:
            cube['rect'].top -= 2 * MOVESPEED
        if cube['dir'] == LEFT:
            cube['rect'].left -= 2 * MOVESPEED
        if cube['dir'] == RIGHT:
            cube['rect'].left += 2 * MOVESPEED
        if cube['rect'].top < 0:
            cube['dir'] = DOWN
        if cube['rect'].bottom > WINDOWHEIGHT:
            cube['dir'] = UP
        if cube['rect'].left < 0:
            cube['dir'] = RIGHT
        if cube['rect'].right > WINDOWWIDTH:
            cube['dir'] = LEFT

    def move(self):
        if cube['dir'] == DOWN and Cube.vector_choise == 0:
            cube['dir'] = VECTOR[randint(0, 3)]
        if cube['dir'] == UP and Cube.vector_choise == 0:
            cube['dir'] = VECTOR[randint(0, 3)]
        if cube['dir'] == LEFT and Cube.vector_choise == 0:
            cube['dir'] = VECTOR[randint(0, 3)]
        if cube['dir'] == RIGHT and Cube.vector_choise == 0:
            cube['dir'] = VECTOR[randint(0, 3)]

    def click(self, click_position, score):
        for cube in cubes:
            if cube['rect'].collidepoint(click_position):
                score += 5
                print('+5')
                cubes.pop(cubes.index(cube))

    def inflate(self, width, height):
        cube['rect'].inflate_ip(width, height)


def new_target():
    shape_choise = random.randint(0, 3)
    if shape_choise == 0:
        Cube.appear()
    else:
        Balloon.appear()

def new_balloon():
    pass

def new_cube():
    list_of_cubes.append(Cube.one_cube)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

balls = []
cubes = []
# user_name = input('Enter user_name: ')

balloon = Balloon.appear(balls)
balls.append(balloon)
Cube.appear(cubes)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            Balloon.click(event.pos, score)
            Cube.click(event.pos, score)
            new_target()
    screen.fill(BLACK)
    for ball in balls:
        Balloon.reflect()
        pygame.draw.ellipse(screen, ball['color'], ball['rect'])
    for cube in cubes:
        Cube.inflate(-1, -1)
        Cube.move()
        Cube.reflect()
        pygame.draw.rect(screen, cube['color'], cube['rect'])
    pygame.display.update()

print('Total score:', score)
Total_score = str(score)
output_score = open('Player table.txt', 'a')
string = [user_name, ' - ', Total_score, ' points', '\n']
output_score.writelines(string)
output_score.close()
pygame.quit()
