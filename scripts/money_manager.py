from text import *

class MoneyManager(object):
    """docstring"""
    UI_balance_settings_file = '../settings/balance_settings.json'

    def __init__(self, balance):
        """Constructor"""
        self.balance = balance
        self.UI_balance = Text(str(self.balance), self.UI_balance_settings_file)

    def update(self, user_activity):
        self.balance += 1/25

    def draw(self, surface):
        balance_text = "Баланс: " + str(int(self.balance))
        self.UI_balance.set_content(balance_text)
        self.UI_balance.draw(surface)
