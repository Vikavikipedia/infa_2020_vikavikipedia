import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((417,417))

rect(screen, (216, 217, 217), (0, 0, 417, 417), 0)
circle(screen, (255, 255, 84), (208.5, 208.5), 104.25, 0)
circle(screen, (0, 0, 0), (208.5, 208.5), 104.25, 1)


circle(screen, (233, 51, 34), (158, 188), 21, 0)
circle(screen, (0, 0, 0), (158, 188), 21, 1)
circle(screen, (0, 0, 0), (158, 188), 8, 0)


circle(screen, (233, 51, 34), (264, 188), 15.5, 0)
circle(screen, (0, 0, 0), (264, 188), 15.5, 1)
circle(screen, (0, 0, 0), (264, 188), 7.5, 0)

polygon(screen, (0, 0, 0),((109, 123), (103, 131), (186, 181), (192, 173)),  0)
polygon(screen, (0, 0, 0),((230, 174), (234, 184), (317, 151), (313, 142)),  0)

rect(screen, (0, 0, 0), (158, 260, 101, 18), 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()