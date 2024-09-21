class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute, can't be accessed directly

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

            

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    # Method to check the balance
    def get_balance(self):
        return self.__balance

# Create a bank account object
my_account = BankAccount(100)  # Starts with a balance of 100

# Use the methods to deposit and withdraw money
my_account.deposit(50)  # Add 50 to balance
my_account.withdraw(30)  # Take 30 from balance

# Check the balance
print(my_account.get_balance())  # Output: 120
