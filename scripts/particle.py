import pygame
from pygame import *
from picture import *
import random

class Particle(object):
    """docstring"""
    ORANGE_01 = (200, 128, 0)
    GREEN = (0, 200, 64)
    ORANGE_02 = (255, 128, 0)

    def __init__(self, start_position, fruit_type):
        """Constructor"""
        self.size = 3
        self.position = (start_position[0]+random.randint(-20, 20), start_position[1]+random.randint(-20, 20))
        if fruit_type == "peach":
            self.color = self.ORANGE_01
        elif fruit_type == "apple":
            self.color = self.GREEN
        else:
            self.color = self.ORANGE_02

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1], self.size, self.size))
        pygame.draw.rect(surface, self.color, rect)
        pass
