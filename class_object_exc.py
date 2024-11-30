class BankAccount:
    def set_details(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Name is: {self.name}, balance is: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


u1 = BankAccount()
u1.set_details("Mirza Haseeb Baig", 100000)


u1.withdraw(25000)

u1.display()