class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
        

    def make_deposit(self,amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self,amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount 
        self.display_user_balance()
        user.display_user_balance()
        return self


kobe = User("Kobe Bryant", "mamba@dojo.com")
mj = User("Michael Jordan", "goat@dojo.com")
ai = User("Allen Iverson", "crossover@dojo.com")

kobe.make_deposit(500).make_deposit(1500).make_deposit(2500).make_withdrawl(1000).display_user_balance()

mj.make_deposit(5000).make_deposit(2500).make_withdrawl(1000).make_withdrawl(1500).display_user_balance()

ai.make_deposit(15000).make_withdrawl(1300).make_withdrawl(1200).make_withdrawl(1600).display_user_balance()

kobe.transfer_money(1000, mj)