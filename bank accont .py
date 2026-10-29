class bankaccont:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,add):
        self.balance +=add
    def withdrow(self,send):
        if ( self.balance>=send):
            self.balance-=send
        else:
            print("your balance is insufficient")
r1=bankaccont("ahmed",0)
print("your name is :",r1.name)

r1.deposit(2000)

r1.withdrow(3000)

print("______________________")
print("your balance is :",r1.balance)