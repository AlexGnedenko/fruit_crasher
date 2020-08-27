from picture import *
from skill_ui import *
import json


class UI(object):
    """docstring"""
    UI_bg_settings_file = "../settings/bg_settings.json"

    UI_skill_rotated_speed_file = "../settings/SKILL_rotated_speed.json"
    UI_skill_n_blades_file = "../settings/SKILL_n_blades.json"
    UI_skill_fruit_generation_file = "../settings/SKILL_fruit_generation.json"
    UI_skill_fruit_type_file = "../settings/SKILL_fruit_type.json"
    UI_skill_coefficient = "../settings/SKILL_coefficient.json"
    SAVE_file = "../settings/SAVE.json"

    def __init__(self):
        """Constructor"""
        # init background image
        self.UI_bg = Picture(self.UI_bg_settings_file)

        # load user save
        with open(self.SAVE_file) as f:
            save = json.load(f)

        # load rotated_speed skill info
        with open(self.UI_skill_rotated_speed_file) as f:
            skill_rotated_speed_info = json.load(f)
        for i in range(1, 9):
            if skill_rotated_speed_info[str(i)]["value"] == save["rotation_speed"]:
                self.UI_skill_rotated_speed = SkillUI("Скорость вращения:", i, skill_rotated_speed_info)

        # load n_blades skill info
        with open(self.UI_skill_n_blades_file) as f:
            skill_n_blades_info = json.load(f)
        for i in range(1, 9):
            if skill_n_blades_info[str(i)]["value"] == save["n_blade"]:
                self.UI_skill_n_blades = SkillUI("Количество лезвий:", i, skill_n_blades_info)

        # load fruit_generation skill info
        with open(self.UI_skill_fruit_generation_file) as f:
            skill_fruit_generation_info = json.load(f)
        for i in range(1, 9):
            if skill_fruit_generation_info[str(i)]["value"] == save["generation_fruit_speed"]:
                self.UI_skill_fruit_generation = SkillUI("Количество фруктов:", i, skill_fruit_generation_info)

        # load fruit_type skill info
        with open(self.UI_skill_fruit_type_file) as f:
            skill_fruit_type_info = json.load(f)
        for i in range(1, 9):
            if skill_fruit_type_info[str(i)]["value"] == save["fruit_quality"]:
                self.UI_skill_fruit_type = SkillUI("Качество фруктов:", i, skill_fruit_type_info)

        # load coefficient skill info
        with open(self.UI_skill_coefficient) as f:
            skill_coefficient_info = json.load(f)
        for i in range(1, 9):
            if skill_coefficient_info[str(i)]["value"] == save["coefficient"]:
                self.UI_skill_coefficient = SkillUI("Стоимость продажи:", i, skill_coefficient_info)

    def update(self, user_activity):
        self.UI_skill_rotated_speed.update(user_activity)
        self.UI_skill_n_blades.update(user_activity)
        self.UI_skill_fruit_generation.update(user_activity)
        self.UI_skill_fruit_type.update(user_activity)
        self.UI_skill_coefficient.update(user_activity)

    def draw(self, surface):
        self.UI_bg.draw(surface)
        self.UI_skill_rotated_speed.draw(surface)
        self.UI_skill_n_blades.draw(surface)
        self.UI_skill_fruit_generation.draw(surface)
        self.UI_skill_fruit_type.draw(surface)
        self.UI_skill_coefficient.draw(surface)
