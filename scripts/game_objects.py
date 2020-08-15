import pygame
from pygame import *
from money_manager import *
from UI import *

class GameObjects(object):
    """docstring"""

    def __init__(self, balance):
        """Constructor"""
        self.money_manager = MoneyManager(balance)
        self.gui = UI()

    def update_state(self, user_activity):
        self.money_manager.update(user_activity)

    def draw(self, surface):
        self.gui.draw(surface)
        self.money_manager.draw(surface)
        pygame.display.update()
