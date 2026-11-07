class BankAccount:
    Holdername = "Harika"
    acc_no = 3217897
    balance = 20000
    
    def deposite(self):
        money = int(input("Enter the money: "))
        self.balance = self.balance + money
        print(self.balance)
        
    def withdrawal(self):
        cash = int(input("Enter cash: "))
        self.balance = self.balance - cash
        print(self.balance)
        
    def display_balance(self):
        print(self.balance)

SBI = BankAccount()

SBI.deposite()
SBI.withdrawal()
SBI.display_balance()