class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        
    # make depsoit
    def deposit(self,amount):
        self.balance += amount
    
    # make withdraw
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -=amount
            return f'The amount withdrawn from your account is:{amount}'
        else:
            return 'Error: Insufficient fund'
    # get current balnce
    def get_balance(self):
        return self.balance
    
