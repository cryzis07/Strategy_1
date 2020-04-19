import style


class Fighter (object):
    def __init__(self, name=None, health=100):
        self.name = name
        self.health = health
        self.style = style.Style()

    def attack(self,attacker,defender):
        self.fighting_style.attack(attacker,defender)

    def defend(self,attacker,defender):
        self.fighting_style.defend(attacker,defender)

class Chelovek(Fighter):
    def __init__(self, name=None,health=100,fighting_style=None):
        super(Chelovek, self).__init__(name,health)
        self.fighting_style = fighting_style

class Zmey(Fighter):
    def __init__(self, name=None,health=100,fighting_style=None):
        super(Zmey, self).__init__(name,health)
        self.fighting_style = fighting_style
