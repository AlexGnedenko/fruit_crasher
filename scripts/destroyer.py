from wheel import *
import json

class Destroyer(object):
    """docstring"""
    UI_left_wheel_settings_file = "../settings/left_wheel_settings.json"
    UI_right_wheel_settings_file = "../settings/right_wheel_settings.json"

    UI_left_blade_settings_file = "../settings/left_blade_settings.json"
    UI_right_blade_settings_file = "../settings/right_blade_settings.json"

    SKILLS_file = "../settings/SKILLS.json"

    def __init__(self):
        """Constructor"""
        with open(self.SKILLS_file) as f:
            settings = json.load(f)
        SKILL_rotation_speed = settings["rotation_speed"]
        SKILL_n_blade = settings["n_blade"]

        self.left_wheel = Wheel(SKILL_rotation_speed, SKILL_n_blade, self.UI_left_wheel_settings_file, self.UI_left_blade_settings_file)
        self.right_wheel = Wheel(SKILL_rotation_speed, SKILL_n_blade, self.UI_right_wheel_settings_file, self.UI_right_blade_settings_file)

    def update(self, user_activity):
        self.left_wheel.update(user_activity, "left")
        self.right_wheel.update(user_activity, "right")

    def draw(self, surface):
        self.left_wheel.draw(surface)
        self.right_wheel.draw(surface)
