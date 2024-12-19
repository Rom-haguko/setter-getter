class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount must be positive!")
            return
        new_balance = self.__balance + amount
        self.set_balance(new_balance)
        print(f"You deposited {amount}. New balance: {self.get_balance()}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds in the account!")
            return
        new_balance = self.__balance - amount
        self.set_balance(new_balance)
        print(f"You withdrew {amount}. New balance: {self.get_balance()}")

    def transfer(self, account, amount):
        if amount > self.__balance:
            print("Insufficient funds for the transfer!")
            return
        self.withdraw(amount)
        account.deposit(amount)
        print(f"You transferred {amount} to another account. New balance: {self.get_balance()}")

if __name__ == "__main__":
    account1 = BankAccount(100)
    account2 = BankAccount(50)

    print("Balance of account 1:", account1.get_balance())
    print("Balance of account 2:", account2.get_balance())

    account1.deposit(50)
    account1.withdraw(30)
    account1.transfer(account2, 70)

    print("Balance of account 1 after all operations:", account1.get_balance())
    print("Balance of account 2 after all operations:", account2.get_balance())
