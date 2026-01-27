#######################################################################################
# Description : Write a Python program to implement a class named BankAccount with the following requirements:
#               The class should contain two instance variables:
#                   Name (Account holder name)
#                   Amount (Account balance)
#               The class should contain one class variable:
#                   ROI (Rate of Interest), initialized to 10.5
#               Define a constructor (__init__) that accepts Name and initial Amount.
#               Implement the following instance methods:
#                   Display() – displays account holder name and current balance
#                   Deposit() – accepts an amount from the user and adds it to balance
#                   Withdraw() – accepts an amount from the user and subtracts it from balance
#                   (Ensure withdrawal is allowed only if sufficient balance exists)
#                   CalculateInterest() – calculates and returns interest using the formula:
#                       Interest = (Amount * ROI) / 100
#               Create multiple objects and demonstrate all methods.
#
#######################################################################################

class BankAccount:
    ROI = 10.5

    def __init__(self,name,amount):
        self.Name = name
        self.Amount = amount
        self.Interest = 0.0
    
    def Display(self):
        print("Account holder name :",self.Name)
        print("Account balance :",self.Amount)

    def Deposit(self,Deposit):
        self.Amount = self.Amount + Deposit

    def Withdraw(self,Amount):
        if(Amount <= self.Amount):
            self.Amount = self.Amount - Amount

    def CalculateIntrest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100

obj1 = BankAccount("Simran",27000)
obj2 = BankAccount("Rekha",27000)

print("Account 1 :")
obj1.Display()
obj1.Deposit(20000)
obj1.Withdraw(30000)
obj1.CalculateIntrest()
print(obj1.Amount)
print(obj1.Interest)
print("*"*20)
print("Account 2 :")
obj2.Display()
obj2.Deposit(20000)
obj2.Withdraw(30000)
obj2.CalculateIntrest()
print(obj2.Amount)
print(obj2.Interest)