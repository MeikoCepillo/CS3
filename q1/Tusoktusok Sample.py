class Tusoktusok:
    sauce = None
    def __init__(self, name):
        self.name = name

    def dip(self, sauce):
        self.sauce = sauce

    def eat(self):
        print("I am eating", self.name)
        if self.sauce != None:
            print("It was dipped in", self.sauce.name, "end it tastes", self.sauce.taste)

class Sauce:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

    def __del__(self):
        print("Ay natapon ang", self.name, "Wala na tuloy")

fishball = Tusoktusok("fishball")
vinegar = Sauce("vinegar", "sour")
fishball.dip(vinegar)
fishball.eat()
kikiam = Tusoktusok("kikiam")
kikiam.eat()
del vinegar
kikiam.dip(vinegar)
