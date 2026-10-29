class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = float(bill_amount)

    def get_name(self):
        return f"Patient Name: {self.__name}"

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return f"Original Bill: ₱{self.__bill_amount:,.2f}"

    def set_bill_amount(self, bill_amount):
        if bill_amount >0:
            self.__bill_amount = bill_amount
        else:
            print("Bill amount must be a positive number")

    def calculate_bill(self):
        return self.__bill_amount

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return f"Final Bill: ₱{super().calculate_bill() * 0.80:,.2f}"

class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return f"Final Bill: ₱{super().calculate_bill() * 0.85:,.2f}"

patient = Patient("Judy M. Valera", 15000)
senior = SeniorPatient("Jairo Vincent M. Cugtas", 15000)
philhealth = PhilHealthPatient("Ryan Meiko L. Cepillo", 15000)



print("Welcome to the Automated Hospital Billing System (AHBS)")
print("-" * 55)

for patients in (patient, senior, philhealth):
    print(patients.get_name())
    print(patients.get_bill_amount())
    print(f"{patients.calculate_bill()}\n")
