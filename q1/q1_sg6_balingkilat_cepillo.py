class Lab:
    def __init__(self, room_number):
        self.room_number = room_number

class Technician:
    def __init__(self, name, assigned_lab = "None"):
        self.name = name
        self.assigned_lab = assigned_lab
    def assign_lab(self, lab_obj):
        self.assigned_lab = lab_obj

chem_lab = Lab("202")
mr_cruz = Technician("Mr. Cruz")
mr_cruz.assign_lab(chem_lab)

print(f"{mr_cruz.name}, you are assigned to Chemistry Laboratory Room {mr_cruz.assigned_lab.room_number}.")        
        

        
