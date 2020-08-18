import pygame
from pygame import *
from money_manager import *
from UI import *
from destroyer import *
from products import *

class GameObjects(object):
    """docstring"""

    def __init__(self, balance):
        """Constructor"""
        self.money_manager = MoneyManager(balance)
        self.gui = UI()
        self.destroyer = Destroyer()
        self.products = Products()


    def update_state(self, user_activity):
        income = self.products.update(user_activity)
        self.money_manager.update(income, user_activity)
        self.destroyer.update(user_activity)

    def draw(self, surface):
        self.gui.draw(surface)
        self.money_manager.draw(surface)
        self.products.draw(surface)
        self.destroyer.draw(surface)
        pygame.display.update()
