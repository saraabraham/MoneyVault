class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,balance,accountName):
        self.balance = balance
        self.name = accountName
        print(f"\n✅ Account '{self.name}' created.\nBalance = ${self.balance:.2f}\n")
    
    def getBalance(self):
         print(f"\nAccount '{self.name}'.\nBalance = ${self.balance:.2f}\n")

    def deposit(self,amount):
         self.balance = self.balance + amount
         print("\n✅ Deposit Complete!")
         self.getBalance()

    def viableTransaction(self,amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(f"❌ Sorry! Account '{self.name}' has a balance of ${self.balance:.2f} only\n")


    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n✅ Withdrawal Complete!")
            self.getBalance()
        except Exception as error:
            print (f"❌ Withdrawal interrupted!.{error}\n")
    
    def transfer(self,amount,accountName):
        try:
            print("\n**********\n\nBeginning Transfer.... 🚀\n")
            self.viableTransaction(amount)
            self.withdraw(amount)
            accountName.deposit(amount)
            print("\n**********\n\n✅ Transfer Complete....\n")
       
        except Exception as error:
            print (f"❌ Transfer interrupted!.{error}\n")

class InterestRewardsAccount(BankAccount):
    
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("\n✅ Deposit Complete!\n")
        self.getBalance()
    
class SavingsAccount(InterestRewardsAccount):
    def __init__(self, balance, accountName,fee):
        super().__init__(balance, accountName)
        self.fee = fee
    
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n✅ Withdrawal Complete!")
            self.getBalance()
        except Exception as error:
            print (f"❌ Withdrawal interrupted!.{error}\n")



    
    
        

