import random

class Programmer:
    def __init__(self):
        self.tech_names = set()

    def add_tech(self, tech_name):
        name = tech_name.lower()
        if name not in self.tech_names:
            self.tech_names.add(name)
        return self

    def get_random_tech(self):
        return random.choice(list(self.tech_names))
