import math
import pygame
from pygame.draw import *

pygame.init()
FPS = 30

ORANGE = (227, 176, 137)
GREEN = (58, 101, 64)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((821, 545))
screen.fill(ORANGE)

tree_1_surface = pygame.Surface((821, 545), pygame.SRCALPHA)
trunk_rectangles = [(405, 283, 29, 89), (406, 172, 27, 99), (278, 320, 9, 61), (278, 241, 9, 70)]
for trunk in trunk_rectangles:
    rect(tree_1_surface, GREEN, trunk, 0)
trunk_polygons = [((419, 162), (400, 155), (419, 99), (438, 105)), ((425, 88), (416, 84), (443, 10), (452, 13)),
                  ((282, 233), (276, 229), (282, 190), (288, 192)), ((287, 183), (284, 179), (291, 123), (294, 125))]
for poly in trunk_polygons:
    polygon(tree_1_surface, GREEN, poly, 0)

branches_coordinate = [(212, 160, 196, 206, 0.14, 0.6), (-110, 38, 512, 293, 0.09, 0.43),
                       (425, 1, 423, 336, 0.53, 0.86), (432, 121, 173, 222, 0.42, 0.8),
                       (125, 145, 156, 200, 0.14, 0.47), (216, 234, 64, 141, 0.2, 0.6),
                       (290, 116, 142, 203, 0.51, 0.9), (284, 203, 67, 130, 0.4, 0.83)]
for branch in branches_coordinate:
    *branch_coord, start_angle, end_angle = branch
    pygame.draw.arc(tree_1_surface, GREEN, branch_coord, math.pi * start_angle, math.pi * end_angle, width=2)

screen.blit(tree_1_surface, (0, 0))


def rotate_leaf(size, coordinate, angle, color=GREEN):
    leaf_surface = pygame.Surface((size), pygame.SRCALPHA)
    ellipse(leaf_surface, color, (0, 0, *size), 0)
    leaf_ellipse = ellipse(leaf_surface, color, (*coordinate, *size), 0)
    rotated_surface = pygame.transform.rotate(leaf_surface, angle)
    screen.blit(rotated_surface, rotated_surface.get_rect(center=leaf_ellipse.center))


coordinates_big = [(207, 72, 160), (224, 76, 160), (242, 83, 160), (259, 90, 160),
                        (291, 95, 160), (291, 188, 160), (315, 193, 160), (339, 204, 160),
                        (536, 53, 20), (563, 49, 20), (577, 41, 20), (593, 32, 20),
                        (608, 32, 20), (493, 161, 20), (515, 151, 20), (536, 148, 20)]
for leaf_big in coordinates_big:
    *leaf_b, angle_b = leaf_big
    rotate_leaf((10, 55), leaf_b, angle_b)
coordinates_small = [(216, 170, 172), (221, 172, 172), (226, 177, 172), (231, 183, 172),
                     (242, 187, 172), (242, 255, 172), (250, 257, 172), (258, 261, 172),
                     (319, 158, 8), (329, 155, 8), (333, 147, 8), (342, 139, 8),
                     (347, 137, 8), (308, 232, 8), (314, 225, 8), (321, 222, 8)]
for leaf_small in coordinates_small:
    *leaf_s, angle_s = leaf_small
    rotate_leaf((4, 39), leaf_s, angle_s)


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
