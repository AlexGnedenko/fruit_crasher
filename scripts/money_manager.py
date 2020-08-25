from text import *

class MoneyManager(object):
    """docstring"""
    UI_balance_settings_file = '../settings/balance_settings.json'
    SKILLS_file = "../settings/SKILLS.json"

    def __init__(self, balance):
        """Constructor"""
        with open(self.SKILLS_file) as f:
            skills = json.load(f)
        self.SKILL_coefficient = skills["coefficient"]
        self.balance = balance
        self.UI_balance = Text(str(self.balance), self.UI_balance_settings_file)

    def update(self, income, user_activity):
        self.balance += income * self.SKILL_coefficient

    def draw(self, surface):
        balance_text = "Баланс: " + str(int(self.balance))
        self.UI_balance.set_content(balance_text)
        self.UI_balance.draw(surface)
