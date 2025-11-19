# Bank account 

class bankAccount():
    def __init__(self, balance, cash):
        self.balance = balance
        self.cash = cash
     
    def deposit(self, cash):
        self.cash = cash
        self.balance += self.cash
        print(f"New balance: {self.balance}")   
        
    def withdraw(self, cash):
        self.cash = cash
        self.balance -= self.cash
        print(f"New balance: {self.balance}")   
        
my_bank_account = bankAccount(0,0) 
my_bank_account.deposit(500)
my_bank_account.withdraw(400)

        