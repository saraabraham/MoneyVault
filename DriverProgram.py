from bank_accounts import *

Kevin = BankAccount(20000,"Kevin")
Sara=BankAccount(20000,"Sara")

Kevin.getBalance()
Sara.getBalance()

Kevin.deposit(500)
Kevin.withdraw(500)
Kevin.withdraw(50000)

Kevin.transfer(200,Sara)
Kevin.transfer(200000,Sara)

Bryan = InterestRewardsAccount(20000,"Bryan")
Bryan.deposit(100)
Bryan.transfer(200,Sara)

Kristef = SavingsAccount(10000,"Kristef",10)
Kristef.withdraw(50000)