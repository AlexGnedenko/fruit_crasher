from picture import *
from frame import *

class UI(object):
    """docstring"""
    UI_bg_settings_file = "../settings/bg_settings.json"
    UI_main_space_frame_settings_file = "../settings/main_space_frame_settings.json"
    UI_balance_space_frame_settings_file = "../settings/balance_space_frame_settings.json"
    UI_updates_space_frame_settings_file = "../settings/updates_space_frame_settings.json"

    def __init__(self):
        """Constructor"""
        self.UI_bg = Picture(self.UI_bg_settings_file)
        self.UI_main_space_frame = Frame(self.UI_main_space_frame_settings_file)
        self.UI_balance_space_frame = Frame(self.UI_balance_space_frame_settings_file)
        self.UI_updates_space_frame = Frame(self.UI_updates_space_frame_settings_file)

    def draw(self, surface):
        self.UI_bg.draw(surface)
        self.UI_main_space_frame.draw(surface)
        self.UI_balance_space_frame.draw(surface)
        self.UI_updates_space_frame.draw(surface)
