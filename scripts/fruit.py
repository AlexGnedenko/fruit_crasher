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

    @staticmethod
    def count_distance(point_1, point_2):
        return ((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2)**(1/2)

    def update(self, user_activity, wheels):
        rotating_speed = wheels[0].SKILL_rotation_speed
        critical_distance = wheels[0].UI_wheel.size[0]//2 + self.fruit.size[0]//2
        left_wheel_position = wheels[0].UI_wheel.position
        right_wheel_position = wheels[1].UI_wheel.position
        left_distance = self.count_distance(self.fruit.position, left_wheel_position)
        right_distance = self.count_distance(self.fruit.position, right_wheel_position)

        # falling physics and loss health
        x_impulse = 5
        y_impulse = 0
        rotating_impulse = 5
        if self.fruit.position[1] < 700:
            if left_distance < critical_distance:
                x_impulse = 0
                y_impulse = rotating_speed
                rotating_impulse += rotating_speed
                self.health -= wheels[0].SKILL_n_blade * wheels[0].SKILL_rotation_speed
            elif right_distance < critical_distance:
                x_impulse = 0
                y_impulse = -rotating_speed
                rotating_impulse -= rotating_speed
                self.health -= wheels[0].SKILL_n_blade * wheels[0].SKILL_rotation_speed

            # application of impulses
            self.fruit.position = (self.fruit.position[0] + y_impulse, self.fruit.position[1] + x_impulse)
            self.fruit.angle += rotating_impulse
            if self.fruit.angle > 360:
                self.fruit.angle -= 360
        else:
            self.is_dead = True

        # destruction of fruits
        if self.health <= 0:
            self.is_dead = True

    def draw(self, surface):
        self.fruit.draw(surface)
