class Warrior:
    def __init__(self, name):
        self.name = name

    def special_move(self):
        print(f"{self.name} swings a mighty sword!")

class Mage:
    def __init__(self, name):
        self.name = name

    def special_move(self):
        print(f"{self.name} casts a powerful spell!")

class Archer:
    def __init__(self, name):
        self.name = name

    def special_move(self):
        print(f"{self.name} shoots a precise arrow!")


def perform_move(character):
    character.special_move()



character1 = Warrior("Warrior")
character2 = Mage("Mage")
character3 = Archer("Archer")

characters = [character1, character2, character3]
for c in characters:
    perform_move(c)
