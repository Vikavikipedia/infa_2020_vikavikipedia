import pygame
from pygame.draw import *
import random
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))

RED = (random.randint(0, 255), 0, 0)
BLUE = (0, 0, random.randint(0, 255))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, (random.randint(0, 255), random.randint(0, 100), random.randint(0, 100)), event.pos, 50)
                pygame.display.update()
            elif event.button == 3:
                circle(screen,  (random.randint(0, 100), random.randint(0, 100), random.randint(0, 255)), event.pos, 50)
                pygame.display.update()

pygame.quit()