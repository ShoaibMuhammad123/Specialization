import bankaccount
def main():
    account1 = bankaccount.BankAccount(500)
    
    print(account1.balance)
    account1.deposit(400)
    print(account1.withdraw(100))
    print(account1.balance)

main()