import pygame
from pygame import *
from money_manager import *
from UI import *
from logic_objects import *
from sounds import *
from ui_frames import *


class GameObjects(object):
    """docstring"""

    def __init__(self, balance):
        """Constructor"""
        self.money_manager = MoneyManager(balance)
        self.gui = UI()
        self.logic_objects = LogicObjects()
        self.gui_frames = UI_frames()
        self.sounds = Sounds()

    def update_state(self, user_activity):
        income = self.logic_objects.update(user_activity)
        self.money_manager.update(income, user_activity)
        self.gui.update(user_activity)
        self.sounds.play(user_activity)

    def draw(self, surface):
        self.gui.draw(surface)
        self.money_manager.draw(surface)
        self.logic_objects.draw(surface)
        self.gui_frames.draw(surface)
        pygame.display.update()

    def play_music(self):
        self.sounds.play_fone_music()
