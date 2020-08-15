import pygame
from pygame import *
import json

class Picture(object):
    """docstring"""

    def __init__(self, settings_file):
        """Constructor"""
        with open(settings_file) as f:
            settings = json.load(f)

        self.size = (settings["size"][0], settings["size"][1])
        self.position = (settings["position"][0], settings["position"][1])
        self.angle = settings["angle"]
        self.picture_path = settings["picture_path"]
        self.picture_surface = pygame.image.load(self.picture_path)

    def draw(self, surface):
        scaled_surface = pygame.transform.scale(self.picture_surface, self.size)
        rotated_surface = pygame.transform.rotate(scaled_surface, self.angle)
        picture_rect = rotated_surface.get_rect(center=self.position)

        surface.blit(rotated_surface, picture_rect)
