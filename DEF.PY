class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("مبلغ غير صالح أو رصيد غير كافٍ")

    def show_balance(self):
        print(f"الرصيد: {self.balance}")


account = BankAccount("Ali", 1000)

account.deposit(500)
account.withdraw(200)
account.show_balance()  # الرصيد: 1300






