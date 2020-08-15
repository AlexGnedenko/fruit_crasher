import pygame
from pygame import *
import json

class Text(object):
    """docstring"""

    def __init__(self, content, settings_file):
        """Constructor"""
        self.content = content

        with open(settings_file) as f:
            settings = json.load(f)

        self.size = (settings["size"][0], settings["size"][1])
        self.position = (settings["position"][0], settings["position"][1])
        self.color = (settings["color"][0], settings["color"][1], settings["color"][2])

    def draw(self, surface):
        font = pygame.font.Font(pygame.font.match_font('timesnewroman'), self.size[1])
        text = font.render(str(int(self.content)), 1, self.color)
        place = text.get_rect(center=self.position)
        surface.blit(text, place)

    def set_content(self, new_content):
        self.content = new_content
