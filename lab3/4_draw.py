import math
import pygame
from pygame.draw import *
import pygame.gfxdraw

pygame.init()
FPS = 30

orange = (227, 176, 137)
green = (58, 101, 64)
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode((821, 545))
screen.fill(orange)

rect(screen, green, (405, 283, 29, 89), 0)
rect(screen, green, (406, 172, 27, 99), 0)
polygon(screen, green, ((419, 162), (400, 155), (419, 99), (438, 105)), 0)
polygon(screen, green, ((425, 88), (416, 84), (443, 10), (452, 13)), 0)

rect(screen, green, (278, 320, 9, 61), 0)
rect(screen, green, (278, 241, 9, 70), 0)
polygon(screen, green, ((282, 233), (276, 229), (282, 190), (288, 192)), 0)
polygon(screen, green, ((287, 183), (284, 179), (291, 123), (294, 125)), 0)


def rotate_leaf(size, coordinate, angle, color=green):
    leaf_surface = pygame.Surface((size), pygame.SRCALPHA)
    ellipse(leaf_surface, color, (0, 0, *size), 0)
    leaf_ellipse = ellipse(leaf_surface, color, (*coordinate, *size), 0)
    rotated_surface = pygame.transform.rotate(leaf_surface, angle)
    screen.blit(rotated_surface, rotated_surface.get_rect(center=leaf_ellipse.center))


coordinates_big_left = [(207, 72), (224, 76), (242, 83), (259, 90), (291, 95),
                        (291, 188), (315, 193), (339, 204)]
for coordinate in coordinates_big_left:
    rotate_leaf((10, 55), coordinate, 160)
coordinates_big_right = [(536, 53), (563, 49), (577, 41), (593, 32), (608, 32),
                         (493, 161), (515, 151), (536, 148)]
for coordinate in coordinates_big_right:
    rotate_leaf((10, 55), coordinate, 20)
coordinates_small_left = [(216, 170), (221, 172), (226, 177), (231, 183), (242, 187),
                          (242, 255), (250, 257), (258, 261)]
for coordinate in coordinates_small_left:
    rotate_leaf((4, 39), coordinate, 172)
coordinates_small_right = [(319, 158), (329, 155), (333, 147), (342, 139), (347, 137),
                           (308, 232), (314, 225), (321, 222)]
for coordinate in coordinates_small_right:
    rotate_leaf((4, 39), coordinate, 8)

pygame.draw.arc(screen, green, (212, 160, 196, 206), start_angle=math.pi*0.14, stop_angle=math.pi*0.6, width=2)
pygame.draw.arc(screen, green, (-110, 38, 512, 293), start_angle=math.pi*0.09, stop_angle=math.pi*0.43, width=2)
pygame.draw.arc(screen, green, (425, 1, 423, 336), start_angle=math.pi*0.53, stop_angle=math.pi*0.86, width=2)
pygame.draw.arc(screen, green, (432, 121, 173, 222), start_angle=math.pi*0.42, stop_angle=math.pi*0.8, width=2)

pygame.draw.arc(screen, green, (125, 145, 156, 200), start_angle=math.pi*0.14, stop_angle=math.pi*0.47, width=2)
pygame.draw.arc(screen, green, (216, 234, 64, 141), start_angle=math.pi*0.2, stop_angle=math.pi*0.6, width=2)
pygame.draw.arc(screen, green, (290, 116, 142, 203), start_angle=math.pi*0.51, stop_angle=math.pi*0.9, width=2)
pygame.draw.arc(screen, green, (284, 203, 67, 130), start_angle=math.pi*0.4, stop_angle=math.pi*0.83, width=2)

panda_surface = pygame.image.load('panda.bmp')
panda_rect = panda_surface.get_rect(center=(568, 339))
screen.blit(panda_surface, panda_rect)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
