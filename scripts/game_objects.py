import pygame
from pygame import *
from money_manager import *
from UI import *
from logic_objects import *

class GameObjects(object):
    """docstring"""

    def __init__(self, balance):
        """Constructor"""
        self.money_manager = MoneyManager(balance)
        self.gui = UI()
        self.logic_objects = LogicObjects()


    def update_state(self, user_activity):
        income = self.logic_objects.update(user_activity)
        self.money_manager.update(income, user_activity)

    def draw(self, surface):
        self.gui.draw(surface)
        self.money_manager.draw(surface)
        self.logic_objects.draw(surface)
        pygame.display.update()
