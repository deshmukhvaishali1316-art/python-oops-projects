class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} जमा झाले. Total: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} काढले. बाकी: {self.balance}")
        else:
            print("Balance कमी आहे!")

    def show_balance(self):
        print(f"{self.name} चा Balance: {self.balance}")

# Use kaise karna
acc1 = BankAccount("Sagar", 1000)
acc1.deposit(500)
acc1.withdraw(300)
acc1.show_balance()