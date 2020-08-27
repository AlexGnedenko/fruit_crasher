from text import *
import pygame
from pygame import *


class SkillUI(object):
    """docstring"""
    UI_skill_rotated_settings_file = '../settings/skill_rotated_settings.json'
    UI_skill_n_blades_settings_file = '../settings/skill_n_blades_settings.json'
    UI_skill_fruit_generation_settings_file = '../settings/skill_fruit_generation_settings.json'
    UI_skill_fruit_type_settings_file = '../settings/skill_fruit_type_settings.json'
    UI_skill_coefficient_settings_file = '../settings/skill_coefficient_settings.json'

    GREY = (150, 150, 150)
    LIGHTGREY = (225, 225, 225)
    BLACK = (0, 0, 0)

    def __init__(self, name, current_level, all_info):
        """Constructor"""
        self.name = name
        self.current_level = current_level
        self.all_info = all_info
        if name == "Скорость вращения:":
            self.UI_name = Text(str(self.name), self.UI_skill_rotated_settings_file)
            self.position = (800, 255)
            self.rect_size = (25, 8)
            self.UI_rects = list()
            self.set_rects()
            self.UI_active_rects = list()
            self.set_active_rects(self.current_level)
        elif name == "Количество лезвий:":
            self.UI_name = Text(str(self.name), self.UI_skill_n_blades_settings_file)
            self.position = (1120, 255)
            self.rect_size = (25, 8)
            self.UI_rects = list()
            self.set_rects()
            self.UI_active_rects = list()
            self.set_active_rects(self.current_level)
        elif name == "Количество фруктов:":
            self.UI_name = Text(str(self.name), self.UI_skill_fruit_generation_settings_file)
            self.position = (800, 425)
            self.rect_size = (25, 8)
            self.UI_rects = list()
            self.set_rects()
            self.UI_active_rects = list()
            self.set_active_rects(self.current_level)
        elif name == "Качество фруктов:":
            self.UI_name = Text(str(self.name), self.UI_skill_fruit_type_settings_file)
            self.position = (1120, 425)
            self.rect_size = (25, 8)
            self.UI_rects = list()
            self.set_rects()
            self.UI_active_rects = list()
            self.set_active_rects(self.current_level)
        elif name == "Стоимость продажи:":
            self.UI_name = Text(str(self.name), self.UI_skill_coefficient_settings_file)
            self.position = (800, 590)
            self.rect_size = (25, 8)
            self.UI_rects = list()
            self.set_rects()
            self.UI_active_rects = list()
            self.set_active_rects(self.current_level)

    def set_rects(self):
        self.UI_rects.append(
            pygame.Rect((self.position[0] - 110, self.position[1] + 35, self.rect_size[0], self.rect_size[1])))
        self.UI_rects.append(
            pygame.Rect((self.position[0] - 80, self.position[1] + 35, self.rect_size[0], self.rect_size[1])))
        self.UI_rects.append(
            pygame.Rect((self.position[0] - 50, self.position[1] + 35, self.rect_size[0], self.rect_size[1])))
        self.UI_rects.append(
            pygame.Rect((self.position[0] - 20, self.position[1] + 35, self.rect_size[0], self.rect_size[1])))
        self.UI_rects.append(
            pygame.Rect((self.position[0] + 10, self.position[1] + 35, self.rect_size[0], self.rect_size[1])))
        self.UI_rects.append(
            pygame.Rect((self.position[0] + 40, self.position[1] + 35, self.rect_size[0], self.rect_size[1])))
        self.UI_rects.append(
            pygame.Rect((self.position[0] + 70, self.position[1] + 35, self.rect_size[0], self.rect_size[1])))

    def set_active_rects(self, level):
        x_pos = 110
        while level > 1:
            self.UI_active_rects.append(
                pygame.Rect((self.position[0] - x_pos + 1, self.position[1] + 36, self.rect_size[0]-2, self.rect_size[1]-2)))
            x_pos -= 30
            level -= 1

    def update(self, user_activity):
        pass

    def draw(self, surface):
        self.UI_name.draw(surface)
        for rect in self.UI_rects:
            pygame.draw.rect(surface, self.GREY, rect)
        for rect in self.UI_active_rects:
            pygame.draw.rect(surface, self.BLACK, rect)

