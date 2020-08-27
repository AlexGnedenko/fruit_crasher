from fruit import *
from wheel import *
from particle import *
import json
import random

class LogicObjects(object):
    """docstring"""
    UI_left_wheel_settings_file = "../settings/left_wheel_settings.json"
    UI_right_wheel_settings_file = "../settings/right_wheel_settings.json"

    UI_left_blade_settings_file = "../settings/left_blade_settings.json"
    UI_right_blade_settings_file = "../settings/right_blade_settings.json"

    SKILLS_file = "../settings/SAVE.json"

    def __init__(self):
        """Constructor"""
        self.particles = list()
        self.fruits = list()
        self.timer = 0

        with open(self.SKILLS_file) as f:
            skills = json.load(f)

        self.SKILL_generation_fruit_speed = skills["generation_fruit_speed"]
        self.SKILL_fruit_quality = skills["fruit_quality"]
        self.SKILL_rotation_speed = skills["rotation_speed"]
        self.SKILL_n_blade = skills["n_blade"]

        self.left_wheel = Wheel(self.SKILL_rotation_speed, self.SKILL_n_blade, self.UI_left_wheel_settings_file,
                                self.UI_left_blade_settings_file)
        self.right_wheel = Wheel(self.SKILL_rotation_speed, self.SKILL_n_blade, self.UI_right_wheel_settings_file,
                                 self.UI_right_blade_settings_file)

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
            fruit.update(user_activity, [self.left_wheel, self.right_wheel])

        income = 0
        # deleting downed fruit
        for fruit in self.fruits:
            if fruit.is_dead:
                income += fruit.max_health//100
                for i in range(10):
                    self.particles.append(Particle(fruit.fruit.position, fruit.type))
                self.fruits.remove(fruit)

        # rotating wheels
        self.left_wheel.update(user_activity, "left")
        self.right_wheel.update(user_activity, "right")

        # falling particles
        for particle in self.particles:
            if particle.position[1]<700:
                particle.position = (particle.position[0], particle.position[1]+random.randint(5, 7))
            else:
                self.particles.remove(particle)

        return income

    def draw(self, surface):
        # draw fruits
        for fruit in self.fruits:
            fruit.draw(surface)

        # draw wheels
        self.left_wheel.draw(surface)
        self.right_wheel.draw(surface)

        # draw particles
        for particle in self.particles:
            particle.draw(surface)
