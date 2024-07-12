class BankAccount:
    def __init__(my, account_number, account_holder, balance=0.0):
        my.account_number = account_number
        my.account_holder = account_holder
        my.balance = balance

    def deposit(my, amount):
            my.balance +=  amount
            print(f"Deposited {amount}\nNew balance is {my.balance}")


    def withdraw(my, amount):
    
            if amount <= my.balance:
                my.balance -= amount
                print(f"Withdrew {amount}\nNew balance is {my.balance}")
            else:
                print("Insufficient Balance")


    def get_balance(my):
        return my.balance

account = BankAccount("12345678", "Asish Behera", 10000.0)
account.deposit(int(input("Enter the deposit Amount: ")))
account.withdraw(int(input("Enter the Withdrawal amount: ")))
print(f"Current balance: {account.get_balance()}")
