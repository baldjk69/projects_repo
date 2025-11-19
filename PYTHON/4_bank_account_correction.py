class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"✅ Deposited: {amount} | New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("⚠️ Insufficient funds! Transaction cancelled.")
            return
        self.balance -= amount
        print(f"💸 Withdrawn: {amount} | New balance: {self.balance}")

# Create account and test
my_bank_account = BankAccount()
my_bank_account.deposit(500)
my_bank_account.withdraw(400)
my_bank_account.withdraw(200)
