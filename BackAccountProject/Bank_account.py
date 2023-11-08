class Bank_account:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        print(f"Successfully created a account named '{self.name}' with balance ${self.balance}.")
    def get_balance(self):
        print(f"The balance of account named '{self.name}' is ${self.balance}.")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount} to the account named :'{self.name}'.")
        else:
            print("Enter a valid amount.")
    def withdrawal(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Successfully withdraw ${amount} from the account named :'{self.name}'.")
        else:
            print(f"Invalid amount!\nYour withdraw balance ${amount} is bigger the your original balance ${self.balance}.")
    def transfer(self, amount, account):
        if amount < self.balance:
            self.balance -= amount
            account.balance += amount
            print("Transfer complete.")
        else:
            print("Transfer interrupted")
            print(
                f"Invalid amount!\nYour transfer balance ${amount} is bigger the your original balance ${self.balance}.")
class Interest_account(Bank_account):
    def deposit(self, amount):
        if amount > 0:
            self.balance +=  (amount + ( amount * 0.10))
            print("Successfully completed the deposit with interest.")
            self.get_balance()
        else:
            print("Error! Check your balance again!.")
class Savings_account(Bank_account):
    def __init__(self, name, initial_balance):
        super().__init__(name, initial_balance)
        self.fee = self.balance * .05
    def withdrawal(self, amount):
        if (amount + self.fee) < self.balance:
            self.balance -= (amount + self.fee)
            print(f"Successfully withdraw ${amount} and extra charge ${self.fee} from the account named :'{self.name}'.")
        else:
            print(f"Invalid amount!\nYour withdraw balance ${amount} is bigger the your original balance ${self.balance}.")


