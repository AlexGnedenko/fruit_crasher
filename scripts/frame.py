import pygame
from pygame import *
import json

class Frame(object):
    """docstring"""

    def __init__(self, settings_file):
        """Constructor"""
        with open(settings_file) as f:
            settings = json.load(f)

        self.size = (settings["size"][0], settings["size"][1])
        self.position = (settings["position"][0], settings["position"][1])
        self.thickness = settings["thickness"]

        self.top_frame_path = settings["top_picture_path"]
        self.bottom_frame_path = settings["bottom_picture_path"]
        self.left_frame_path = settings["left_picture_path"]
        self.right_frame_path = settings["right_picture_path"]

        self.top_frame_surface = pygame.image.load(self.top_frame_path)
        self.bottom_frame_surface = pygame.image.load(self.bottom_frame_path)
        self.left_frame_surface = pygame.image.load(self.left_frame_path)
        self.right_frame_surface = pygame.image.load(self.right_frame_path)

    def draw(self, surface):
        # top limit
        top_scaled_surface = pygame.transform.scale(self.top_frame_surface, (self.size[0], self.thickness))
        center = (self.position[0], self.position[1] - self.size[1]//2 + self.thickness//2)
        top_picture_rect = top_scaled_surface.get_rect(center=center)

        # bottom limit
        bottom_scaled_surface = pygame.transform.scale(self.bottom_frame_surface, (self.size[0], self.thickness))
        center = (self.position[0], self.position[1] + self.size[1]//2 - self.thickness//2)
        bottom_picture_rect = bottom_scaled_surface.get_rect(center=center)

        # left limit
        left_scaled_surface = pygame.transform.scale(self.left_frame_surface, (self.thickness, self.size[1]))
        center = (self.position[0] - self.size[0]//2 + self.thickness//2, self.position[1])
        left_picture_rect = left_scaled_surface.get_rect(center=center)

        # right limit
        right_scaled_surface = pygame.transform.scale(self.right_frame_surface, (self.thickness, self.size[1]))
        center = (self.position[0] + self.size[0] // 2 - self.thickness // 2, self.position[1])
        right_picture_rect = right_scaled_surface.get_rect(center=center)

        surface.blit(top_scaled_surface, top_picture_rect)
        surface.blit(bottom_scaled_surface, bottom_picture_rect)
        surface.blit(left_scaled_surface, left_picture_rect)
        surface.blit(right_scaled_surface, right_picture_rect)
