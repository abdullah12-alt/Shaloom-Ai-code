class ATM:
    def __init__(self,balance=0):
        self.balance = balance


    def deposit(self,amount):
        if amount <= 0:
            return "Invalid amount. Deposit amount must be positive."
        self.balance += amount
        return f"${amount} deposited successfully. New balance: ${self.balance}"

    def withdraw(self,amount):
        if amount <= 0:
            return "Invalid amount. Withdrawal amount must be positive."
        if amount > self.balance:
            return "Insufficient funds. Withdrawal amount exceeds balance."
        self.balance -= amount
        return f"${amount} withdrawn successfully. New balance: ${self.balance}"
    
    def __str__(self):
        print( f"ATM Balance: ${self.balance}")


def display_menu():
    print("**** ATM Menu ****")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")


# Example usage
my_atm = ATM(500)

while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(my_atm)
    elif choice == '2':
        amount = float(input("Enter the deposit amount: $"))
        print(my_atm.deposit(amount))
    elif choice == '3':
        amount = float(input("Enter the withdrawal amount: $"))
        print(my_atm.withdraw(amount))
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")