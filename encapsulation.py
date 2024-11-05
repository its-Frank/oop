"""
Create a class named BankAccount with a private attribute balance. 
Add methods deposit() and withdraw() to adjust the balance, ensuring balance can’t be directly accessed or modified outside the class. 
Write code to demonstrate depositing and withdrawing money while maintaining encapsulation.
"""
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds.")

# Create an instance of the BankAccount class
my_account = BankAccount(1000)

# Deposit and withdraw money
my_account.deposit(500)
my_account.withdraw(200)
my_account.withdraw(2000)

# Trying to access the balance directly (this won't work)
# print(my_account.__balance)