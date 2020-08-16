from picture import *

class Wheel(object):
    """docstring"""

    def __init__(self, SKILL_rotation_speed, setting_file):
        """Constructor"""
        self.SKILL_rotation_speed = SKILL_rotation_speed
        self.UI_wheel = Picture(setting_file)

    def update(self, user_activity, direction):
        if direction == "right":
            self.UI_wheel.angle += self.SKILL_rotation_speed
            if self.UI_wheel.angle > 360:
                self.UI_wheel.angle -= 360
        else:
            self.UI_wheel.angle -= self.SKILL_rotation_speed
            if self.UI_wheel.angle < -360:
                self.UI_wheel.angle += 360

    def draw(self, surface):
        self.UI_wheel.draw(surface)
