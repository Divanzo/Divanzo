class BankAccount:
    def __init__(self,acnt):
        self.acnt=acnt
        self.balance=0

    def deposit(self,amt):
        self.balance+=amt
        print(f'{self.acnt} 통장에 {amt}원이 입금됨')
        print(f'현재 잔액은 {self.balance}')

    def withdraw(self,amt):
        self.balance-=amt
        print(f'{self.acnt} 통장에 {amt}원이 이체됨')
        print(f'현재 잔액은 {self.balance}')
        

a=BankAccount('123-456')
a.deposit(10000)
a.withdraw(3000)

b=BankAccount('456-789')
b.deposit(2000)
