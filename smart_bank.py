# Ek hi Concept se pura Bank System

class MobileSMS:
    def send_sms(self, msg):
        print(f"\n📱 [MOBILE MESSAGE]: {msg}\n")

class BankAccount(MobileSMS): # Inheritance - Bank ko SMS ka power diya
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f"Account khula: {name} ke liye")

    def deposit(self, amount):
        self.balance += amount
        self.send_sms(f"Rs.{amount} jama hue. Total Balance: Rs.{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.send_sms(f"Paise nahi hai! Balance sirf Rs.{self.balance} hai")
        else:
            self.balance -= amount
            self.send_sms(f"Rs.{amount} nikale gaye. Bacha Balance: Rs.{self.balance}")

    def show_balance(self):
        print(f"Current Balance: Rs.{self.balance}")

# --- Yaha se code लगातार chalega ---
print("--- Smart Bank Start ---")
user = BankAccount("Vaishali", 1000)

while True:
    print("\n1. Paise Dalna (Deposit)")
    print("2. Paise Nikalna (Withdraw)")
    print("3. Balance Dekhna")
    print("4. Band Karo")
    
    choice = input("Kya karna hai (1-4): ")

    if choice == '1':
        amt = int(input("Kitne dalne hai? "))
        user.deposit(amt)
    elif choice == '2':
        amt = int(input("Kitne nikalne hai? "))
        user.withdraw(amt)
    elif choice == '3':
        user.show_balance()
    elif choice == '4':
        print("Bank Band. Bye!")
        break