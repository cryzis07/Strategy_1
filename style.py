class Style(object):
    def attack(self, opponent):
        pass
    def defend(self, attacker):
        pass

class  KulachniiBoi(Style):
    def __init__(self):
        super(KulachniiBoi,self).__init__()

    def attack(self, attacker, opponent):
        message = '{0.name} attacking {1.name} in KulachniiBoi style'.format(attacker, opponent)
        print(message)
    def defend(self,attacker, opponent):
        message = '{0.name} defending {1.name} in KulachniiBoi style'.format(attacker, opponent)
        print(message)
class Cheshuya(Style):
    def __init__(self):
        super(Cheshuya,self).__init__()

    def attack(self, attacker, opponent):
        message = '{0.name} attacking {1.name} in Cheshuya style'.format(attacker, opponent)
        print(message)
    def defend(self,attacker, opponent):
        message = '{0.name} defending {1.name} in Cheshuya style'.format(attacker, opponent)
        print(message)
