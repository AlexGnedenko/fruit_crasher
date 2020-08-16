from picture import *

class Wheel(object):
    """docstring"""

    def __init__(self, SKILL_rotation_speed, SKILL_n_blade, wheel_setting_file, blade_setting_file):
        """Constructor"""
        # creating wheel
        self.SKILL_rotation_speed = SKILL_rotation_speed
        self.UI_wheel = Picture(wheel_setting_file)

        # creating blade
        self.SKILL_n_blade = SKILL_n_blade
        self.UI_blade = []
        for i in range(self.SKILL_n_blade):
            self.UI_blade.append(Picture(blade_setting_file))

        # set blade angles
        angle_step = 180//self.SKILL_n_blade
        for i in range(self.SKILL_n_blade):
            self.UI_blade[i].angle = i*angle_step

    def update(self, user_activity, direction):
        if direction == "right":
            # rotate wheel
            self.UI_wheel.angle += self.SKILL_rotation_speed
            if self.UI_wheel.angle > 360:
                self.UI_wheel.angle -= 360

            # rotate blade
            for blade in self.UI_blade:
                blade.angle += self.SKILL_rotation_speed
                if blade.angle > 360:
                    blade.angle -= 360
        else:
            # rotate wheel
            self.UI_wheel.angle -= self.SKILL_rotation_speed
            if self.UI_wheel.angle < -360:
                self.UI_wheel.angle += 360

            # rotate blade
            for blade in self.UI_blade:
                blade.angle -= self.SKILL_rotation_speed
                if blade.angle < -360:
                    blade.angle += 360

    def draw(self, surface):
        for blade in self.UI_blade:
            blade.draw(surface)
        self.UI_wheel.draw(surface)
