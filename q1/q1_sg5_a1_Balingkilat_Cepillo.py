class Hero:
    def __init__(self, name, hp = 100):
        self.name = name
        self.hp = hp
    def take_damage(self, amount=10):
        self.hp -= amount
        

hero1 = Hero("Arthur")
hero2 = Hero("Morgana")

Arthur = hero1.take_damage()

print("Arthur has", hero1.hp)
print("Morgana has", hero2.hp)
