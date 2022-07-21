import random as rnd
import math
import pygame

from my_colors import *

FPS = 20
GRAVITY_ACCELERATION = 9.8
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800


class Cannon:
    max_velocity = 10

    def __init__(self, x, y):
        pass

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (int(round(self.x)), int(round(self.y))), self.r)


    def aim(self, x, y):
        pass

    def fire(self, dt):
        pass


class Shell:
    standart_radius = 25

    def __init__(self, x, y, Vx, Vy):
        self.x, self.y = x, y
        self.Vx, self.Vy = Vx, Vy
        self.r = Shell.standart_radius

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (int(round(self.x)), int(round(self.y))), self.r)


    def move(self, dt):
        pass

    def detect_collision(self, other):
        pass


class Target:
    standart_radius = 15

    def __init__(self, x, y, Vx, Vy):
        pass

    def move(self, dt):
        pass

    def draw(self):
        pygame.draw.circle(screen, self.color,
                           (int(round(self.x)), int(round(self.y))), self.r)

    def collide(self, other):
        pass


class Bomb:
    pass
