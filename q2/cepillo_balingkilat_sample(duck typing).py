class Vehicle:
    color = "Thermalite Gray"
    def __init__(self, name, passengers):
        self.name = name
        self.passengers = passengers

    def move(self):
        print(f"Vehicle {self.color} {self.name} is moving")
        print(f"It has {self.passengers} passengers")

class Car(Vehicle):
    def move(self):
        print(f"Car {self.color} {self.name} is moving on the road")
        print(f"It has {self.passengers} passengers")

class Boat(Vehicle):
    def move(self):
        print(f"Boat {self.color} {self.name} is floating on the water")
        print(f"It has {self.passengers} passengers")

class Toilet:
    color = "brown"
    name = "Skividi Toilet"
    passengers = 1
    def move(self):
        print(f"Toilet {self.color} {self.name} is flushing")
        print(f"It has {self.passengers} passengers. You.")
        

car = Car("Toyota Innova", 7)
car2 = Car("BYD Seal", 5)
car2.color = "Ocean Blue"
boat = Boat("Kayak", 3)
boat.color = "Red"
toilet = Toilet()

vehicles = [car, car2, boat, toilet]
for v in vehicles:
    v.move()
