import pygame
from pygame import *


class Sounds(object):
    """docstring"""
    fone_music_file = "../sounds/fone_music.mp3"
    button_sound_file = "../sounds/tap.ogg"

    def __init__(self):
        """Constructor"""
        pygame.mixer.music.load(self.fone_music_file)
        self.button_sound = pygame.mixer.Sound(self.button_sound_file)

    def play(self, user_activity):
        if user_activity[K_SPACE]:
            self.play_button_sound()

    def play_fone_music(self):
        pygame.mixer.music.play(-1)

    def play_button_sound(self):
        self.button_sound.play()
