import math

import pygame
from pygame.draw import *

pygame.init()
FPS = 30

# Setting colors
ORANGE = (243, 178, 135)
GREEN = (43, 102, 60)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Drawing background with dimensions SIZE and color ORANGE
SIZE = (821, 545)
X, Y = SIZE
screen = pygame.display.set_mode(SIZE)
screen.fill(ORANGE)

# Creating a surfaces for drawing tree trunks and crowns with dimensions SIZE
tree_surface = pygame.Surface(SIZE, pygame.SRCALPHA)
crown_surface = pygame.Surface(SIZE, pygame.SRCALPHA)


def rotate_leaf(size, coordinate, angle, color=GREEN):
    """This function creates surface for drawing leaves of a given size
    and draws leaves inscribed in a rectangle and rotated at a given angle.
    The leaf coordinate is the coordinate of the center of the ellipse.
    The function add leaf_surface on crown_surface.

    """
    leaf_surface = pygame.Surface(size, pygame.SRCALPHA)
    ellipse(leaf_surface, color, (0, 0, *size), 0)
    leaf_ellipse = ellipse(leaf_surface, color, (*coordinate, *size), 0)
    rotated_surface = pygame.transform.rotate(leaf_surface, angle)
    crown_surface.blit(rotated_surface, rotated_surface.get_rect(center=leaf_ellipse.center))
    screen.blit(crown_surface, (0, 0))


# List of leaf coordinates contains dimensions of rectangles and angles of rotation
leaf_coordinates = [(207, 72, 160), (224, 76, 160), (242, 83, 160), (259, 90, 160),
                    (291, 95, 160), (291, 188, 160), (315, 193, 160), (339, 204, 160),
                    (536, 53, 20), (563, 49, 20), (577, 41, 20), (593, 32, 20),
                    (608, 32, 20), (493, 161, 20), (515, 151, 20), (536, 148, 20)]
# Drawing leaves of the largest tree
for leaf in leaf_coordinates:
    *leaf_rectangle, leaf_angle = leaf
    rotate_leaf((10, 55), leaf_rectangle, leaf_angle)

# Drawing trunk of the largest tree with Rectangles and Polygons
trunk_rectangles = [(405, 283, 29, 89), (406, 172, 27, 99)]
for trunk in trunk_rectangles:
    rect(tree_surface, GREEN, trunk, 0)
trunk_polygons = [((419, 162), (400, 155), (419, 99), (438, 105)),
                  ((425, 88), (416, 84), (443, 10), (452, 13))]
for poly in trunk_polygons:
    polygon(tree_surface, GREEN, poly, 0)

# Drawing Branches of the largest Tree Using Ellipse Arcs
branches_coordinates = [(212, 160, 196, 206, 0.14, 0.6), (-110, 38, 512, 293, 0.09, 0.43),
                        (425, 1, 423, 336, 0.53, 0.86), (432, 121, 173, 222, 0.42, 0.8)]
for branch in branches_coordinates:
    *branch_coord, start_angle, end_angle = branch
    pygame.draw.arc(tree_surface, GREEN, branch_coord, math.pi * start_angle, math.pi * end_angle,
                    width=2)

screen.blit(tree_surface, (0, 0))

# Drawing little trees.
# x_tree and y_tree are coordinates of the left top angle of the whole tree
# nx and ny are scaling factors relative to the largest tree.
transformation_ratios = [(0.407, 0.6, -53.428, 157.2),
                         (0.333, 0.716, 144.468, 118.512),
                         (0.45, 0.875, 538.2, 28)]
for ratio in transformation_ratios:
    nx, ny, x_tree, y_tree = ratio
    tree_surf = pygame.Surface(SIZE, pygame.SRCALPHA)
    transformed_trunk = pygame.transform.scale(tree_surface, (X * nx, Y * ny))
    transformed_crown = pygame.transform.scale(crown_surface, (X * nx, Y * ny))
    screen.blit(transformed_trunk, (x_tree, y_tree))
    screen.blit(transformed_crown, (x_tree, y_tree))

# Drawing pandas at given coordinates with by adding files panda.bmp and baby_panda.bmp
panda_surf_1 = pygame.image.load('panda.bmp')
panda_rect_1 = panda_surf_1.get_rect(center=(568, 339))
screen.blit(panda_surf_1, panda_rect_1)

panda_surf_2 = pygame.image.load('baby_panda.bmp')
panda_rect_2 = pygame.transform.scale(panda_surf_2, (126, 98))
screen.blit(panda_rect_2, (335, 385))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
