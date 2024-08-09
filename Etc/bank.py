class Account: 
    def __init__(self):
        self._balance = 0
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount
        
    def withdraw(self, amount):
        self._balance -= amount
        
    
def main():
    account = Account()
    print(f"Balance: {account.balance}")
    account.deposit(1000)
    account.withdraw(500)
    print(f"Balance: {account.balance}")
    
if __name__ == "__main__":
    main()