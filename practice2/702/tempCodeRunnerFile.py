class Account:
    def deposit(self, amount):
        if amount > 0:
            self.deposit = amount
    
    def withdraw(self, amount):
        self.withdraw = amount
        if self.deposit < self.withdraw:
            print("Insufficient Funds")
        else:
            print(self.deposit - self.withdraw)    
a,b = map(int,input().split())
acc = Account()
acc.deposit(a)
acc.withdraw(b)