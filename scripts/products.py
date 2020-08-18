from fruit import *
import json
import random

class Products(object):
    """docstring"""
    SKILLS_file = "../settings/SKILLS.json"

    def __init__(self):
        """Constructor"""
        self.fruits = list()
        self.timer = 0

        with open(self.SKILLS_file) as f:
            skills = json.load(f)
        self.SKILL_generation_fruit_speed = skills["generation_fruit_speed"]
        self.SKILL_fruit_quality = skills["fruit_quality"]

    def generate_new_fruit(self):
        fruit_type = random.choice(self.SKILL_fruit_quality)
        self.fruits.append(Fruit(fruit_type))

    def update(self, user_activity):
        # creating new fruits
        if self.timer % self.SKILL_generation_fruit_speed == 0:
            self.generate_new_fruit()

        # increment timer
        self.timer += 1

        # update exist fruits
        for fruit in self.fruits:
            fruit.update(user_activity)

        income = 0
        # deleting downed fruit
        for fruit in self.fruits:
            if fruit.is_dead:
                income += fruit.max_health//100
                self.fruits.remove(fruit)

        return income

    def draw(self, surface):
        for fruit in self.fruits:
            fruit.draw(surface)
