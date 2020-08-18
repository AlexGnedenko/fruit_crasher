from picture import *
import json
import random

class Fruit(object):
    """docstring"""

    peach_setting_file = "../settings/peach_settings.json"
    apple_setting_file = "../settings/apple_settings.json"
    orange_setting_file = "../settings/orange_settings.json"

    def __init__(self, fruit_type):
        """Constructor"""
        if fruit_type == 0:
            self.type = "peach"
            self.fruit = Picture(self.peach_setting_file)
            self.max_health = 100
            self.health = 100
            self.is_dead = False
            self.fruit.position = (random.randint(50, 590), self.fruit.position[1])
        elif fruit_type == 1:
            self.type = "apple"
            self.fruit = Picture(self.apple_setting_file)
            self.max_health = 500
            self.health = 500
            self.is_dead = False
            self.fruit.position = (random.randint(50, 590), self.fruit.position[1])
        else:
            self.type = "orange"
            self.fruit = Picture(self.orange_setting_file)
            self.max_health = 1000
            self.health = 1000
            self.is_dead = False
            self.fruit.position = (random.randint(50, 590), self.fruit.position[1])

    def update(self, user_activity):
        if self.fruit.position[1] < 700:
            # falling fruits
            self.fruit.position = (self.fruit.position[0], self.fruit.position[1] + 5)

            # rotating fruits
            self.fruit.angle += random.randint(2, 10)
            if self.fruit.angle > 360:
                self.fruit.angle -= 360
        else:
            self.is_dead = True

    def draw(self, surface):
        self.fruit.draw(surface)
