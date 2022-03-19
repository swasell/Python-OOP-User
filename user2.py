class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawl(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount 
        self.display_user_balance()
        user.display_user_balance()


kobe = User("Kobe Bryant", "mamba@dojo.com")
mj = User("Michael Jordan", "goat@dojo.com")
ai = User("Allen Iverson", "crossover@dojo.com")

kobe.make_deposit(500)
kobe.make_deposit(1500)
kobe.make_deposit(2500)
kobe.make_withdrawl(1000)
kobe.display_user_balance()

mj.make_deposit(5000)
mj.make_deposit(2500)
mj.make_withdrawl(1000)
mj.make_withdrawl(1500)
mj.display_user_balance()

ai.make_deposit(15000)
ai.make_withdrawl(1300)
ai.make_withdrawl(1200)
ai.make_withdrawl(1600)
ai.display_user_balance()

kobe.transfer_money(1000, mj)