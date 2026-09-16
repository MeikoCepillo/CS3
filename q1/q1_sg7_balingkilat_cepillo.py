class Glassware:
    def __init__(self, volume):
        self.volume = volume

class Beaker(Glassware):
    def __init__(self, volume, brand, marginOfError):
        super().__init__(volume)
        self.brand = brand
        self.marginOfError = marginOfError

    def chem(self, chemical):
        print(f"{chemical} is stored in this beaker")

class Tray:
    def __init__(self, number):
        self.number = number
        self.beakers = [
            Beaker(10, "Pyrex", 0.50),
            Beaker(10, "Glassco", 1.00),
            Beaker(10, "Kimax", 2.00),
            Beaker(10, "Duran", 0.05),
            Beaker(10, "Brosil", 5.00)
        ]

    def __del__(self):
        for beaker in self.beakers:
            print(f"Beaker {beaker.brand} is now gone")

cabinet = Tray("T1")
del cabinet

