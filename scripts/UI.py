from picture import *

class UI(object):
    """docstring"""
    UI_bg_settings_file = "../settings/bg_settings.json"

    def __init__(self):
        """Constructor"""
        self.UI_bg = Picture(self.UI_bg_settings_file)

    def draw(self, surface):
        self.UI_bg.draw(surface)
