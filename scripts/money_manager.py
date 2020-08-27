from text import *
import json

class MoneyManager(object):
    """docstring"""
    UI_balance_settings_file = '../settings/balance_settings.json'
    SKILLS_file = "../settings/SAVE.json"

    def __init__(self, balance):
        """Constructor"""
        with open(self.SKILLS_file) as f:
            skills = json.load(f)
        self.SKILL_coefficient = skills["coefficient"]
        self.balance = balance
        self.UI_balance = Text(str(self.balance), self.UI_balance_settings_file)

    def update(self, income, user_activity):
        # set balance variable
        self.balance += income * self.SKILL_coefficient

        # save new balance
        with open(self.SKILLS_file) as f:
            skills = json.load(f)
        skills["balance"] = self.balance
        with open(self.SKILLS_file, 'w') as file:
            json.dump(skills, file)

    def draw(self, surface):
        balance_text = "Баланс: " + str(int(self.balance))
        self.UI_balance.set_content(balance_text)
        self.UI_balance.draw(surface)
