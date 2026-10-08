class Account:
    name = ""
    number = ""
    __balance = 0
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount

    def __str__(self):
        return self.name + "[" + self.number + "] P" + str(self.__balance)

    def __del__(self):
        print("Account", self.number, "closed")

class SavingsAccount(Account):
    __interest = 0.05
    def addInterest(self):
        interestToAdd = super().getBalance() * self.__interest
        super().deposit(interestToAdd)

class Bank:
    name = ""
    __accounts = []
    def __init__(self, name):
        self.name = name
        print("Welcome to", self.name)

    def openAccount(self):
        print("Ready to open an account")
        acc_name = input("Account name: ")
        acc_number = input("Account number: ")
        acc_type = input("Account type (savings or checking): ")
        if acc_type == "savings":
            account = SavingsAccount(acc_name, acc_number)
        else:
            account = Account(acc_name, acc_number)
        print("Account created")
        print(account)
        self.__accounts.append(account)

    def showAccounts(self):
        print("Showing accounts")
        for a in self.__accounts:
            print(a)

    def deposit(self):
        print("Ready to deposit an amount")
        amount = float(input("Enter amount to deposit: "))
        print(f"You are about to deposit an amount of P {amount}")
        acc_number = input("Enter account number: ")
        for a in self.__accounts:
            if a.number == acc_number:
                a.deposit(amount)
                print("Deposit Successful")
                print(a)

    def addInterest(self):
        print("Adding interest to all savings accounts")
        for a in self.__accounts:
            if isinstance(a, SavingsAccount):
                a.addInterest()
                print("Interest added to account", a.number)
                print(a)

    def closeAccount(self):
        print("Ready to close an account")
        acc_number = input("Enter account number: ")
        for a in self.__accounts:
            if a.number == acc_number:
                self.__accounts.remove(a)
                del a
                print("Account closed")

    def __del__(self):
        print("Thank you for banking with", self.name)
        for a in self.__accounts:
            self.__accounts.remove(a)
            del a
        
bank = Bank("Land Bank of the Philippines")
bank.openAccount()
bank.openAccount()
bank.showAccounts()
bank.deposit()
bank.addInterest()
bank.closeAccount()
del bank
