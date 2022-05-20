import math
import pygame
from pygame.draw import *
from pygame.surface import Surface, SurfaceType

pygame.init()
FPS = 30

ORANGE = (227, 176, 137)
GREEN = (58, 101, 64)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SIZE = (821, 545)
X, Y = SIZE
screen = pygame.display.set_mode(SIZE)
screen.fill(ORANGE)

tree_surface = pygame.Surface(SIZE, pygame.SRCALPHA)
X_tree = 404
Y_tree = 368
crown_serf = pygame.Surface(SIZE, pygame.SRCALPHA)


def rotate_leaf(size, coordinate, angle, color=GREEN):
    leaf_surface = pygame.Surface(size, pygame.SRCALPHA)
    ellipse(leaf_surface, color, (0, 0, *size), 0)
    leaf_ellipse = ellipse(leaf_surface, color, (*coordinate, *size), 0)
    rotated_surf = pygame.transform.rotate(leaf_surface, angle)
    crown_serf.blit(rotated_surf, rotated_surf.get_rect(center=leaf_ellipse.center))
    screen.blit(crown_serf, (0, 0))


leaf_coordinates = [(207, 72, 160), (224, 76, 160), (242, 83, 160), (259, 90, 160),
                    (291, 95, 160), (291, 188, 160), (315, 193, 160), (339, 204, 160),
                    (536, 53, 20), (563, 49, 20), (577, 41, 20), (593, 32, 20),
                    (608, 32, 20), (493, 161, 20), (515, 151, 20), (536, 148, 20)]
for leaf in leaf_coordinates:
    *leaf_rec, leaf_angle = leaf
    rotate_leaf((10, 55), leaf_rec, leaf_angle)


trunk_rectangles = [(405, 283, 29, 89), (406, 172, 27, 99)]
for trunk in trunk_rectangles:
    rect(tree_surface, GREEN, trunk, 0)
trunk_polygons = [((419, 162), (400, 155), (419, 99), (438, 105)),
                  ((425, 88), (416, 84), (443, 10), (452, 13))]
for poly in trunk_polygons:
    polygon(tree_surface, GREEN, poly, 0)

branches_coordinate = [(212, 160, 196, 206, 0.14, 0.6), (-110, 38, 512, 293, 0.09, 0.43),   # ветки
                       (425, 1, 423, 336, 0.53, 0.86), (432, 121, 173, 222, 0.42, 0.8)]
for branch in branches_coordinate:
    *branch_coord, start_angle, end_angle = branch
    pygame.draw.arc(tree_surface, GREEN, branch_coord, math.pi * start_angle, math.pi * end_angle, width=2)

screen.blit(tree_surface, (0, 0))

nx_2 = 0.333    # коэффициент сжатия для 2 пальмы
ny_2 = 0.716
x_tree_2 = 279  # координаты ствола 2 пальмы
y_tree_2 = 382
tree_surf_2 = pygame.Surface(SIZE, pygame.SRCALPHA)
trunk_2 = pygame.transform.scale(tree_surface, (X * nx_2, Y * ny_2))
crown_2: Surface | SurfaceType = pygame.transform.scale(crown_serf, (X * nx_2, Y * ny_2))
screen.blit(trunk_2, (x_tree_2 - X_tree * nx_2, y_tree_2 - Y_tree * ny_2))
screen.blit(crown_2, (x_tree_2 - X_tree * nx_2, y_tree_2 - Y_tree * ny_2))

panda_surf_1 = pygame.image.load('panda.bmp')
panda_rect = panda_surf_1.get_rect(center=(568, 339))
screen.blit(panda_surf_1, panda_rect)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
