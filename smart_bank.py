# Ek hi Concept se pura Bank System

class MobileSMS:
    def send_sms(self, msg):
        print(f"\n📱 [MOBILE MESSAGE]: {msg}\n")

class BankAccount(MobileSMS): # Inheritance - Bank ko SMS ka power diya
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"Account Open: {name}")

    def deposit(self, amount):
        self.balance += amount
        self.send_sms(f"Rs.{amount} Deposited Successfully . Total Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.send_sms(f"There is No Money in Your Accont! Your Bank Balance Only Rs.{self.balance} hai")
        else:
            self.balance -= amount
            self.send_sms(f"Rs.{amount} Withdraw Successfully. Bank Balance: Rs.{self.balance}")

    def show_balance(self):
        print(f"Current Balance: Rs.{self.balance}")

# --- code start
print("--- Smart Bank Start ---")
user = BankAccount("Vaishali", 1000)

while True:
    print("\n1.Deposit Cash")
    print("2. Withdraw Cash")
    print("3. Check Bank Balance ")
    print("4. Close Account")
    
    choice = input(" Choise Your Action (1-4): ")

    if choice == '1':
        amt = int(input("Deposite Amount? "))
        user.deposit(amt)
    elif choice == '2':
        amt = int(input("Withdraw amount? "))
        user.withdraw(amt)
    elif choice == '3':
        user.show_balance()
    elif choice == '4':
        print("Bank account close permanantly , thank you ")
        break