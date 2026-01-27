################################################################################################################
#
# Description : Write a Python program to implement a class named Arithmetic with the following characteristics:
#               The class should contain two instance variables: Value1 and Value2.
#               Define a constructor (__init__) that initializes all instance variables to 0.
#               Implement the following instance methods:
#               Accept() – accepts values for Value1 and Value2 from the user.
#               Addition() – returns the addition of Value1 and Value2.
#               Subtraction() – returns the subtraction of Value1 and Value2.
#               Multiplication() – returns the multiplication of Value1 and Value2.
#               Division() – returns the division of Value1 and Value2 (handle division by zero properly).
#               Create multiple objects of the Arithmetic class and invoke all the instance methods.
#
################################################################################################################
class Arithematic:
    def __init__(self):
        self.No1 = 0
        self.No2 = 0

    def Accept(self):
        self.No1 = int(input("Enter first number : "))
        self.No2 = int(input("Enter second number : "))

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
    def Multiplication(self):
        Ans = 0
        Ans = self.No1 * self.No2
        return Ans
    
    def Division(self):
        Ans = 0
        Ans = self.No1 / self.No2
        return Ans
    
Ret = 0

obj1 = Arithematic()
obj2 = Arithematic()
obj3 = Arithematic()

print("obj1 - ")
obj1.Accept()
print("obj2 - ")
obj2.Accept()
print("obj3 - ")
obj3.Accept()

print("-------------for obj1----------------")
Ret = obj1.Addition()
print("Addition is :",Ret)
Ret = obj1.Substraction()
print("Substraction is :",Ret)
Ret = obj1.Multiplication()
print("Multiplication is :",Ret)
Ret = obj1.Division()
print("Division is :",Ret)
print("-------------------------------------")

print("-------------for obj1----------------")
Ret = obj2.Addition()
print("Addition is :",Ret)
Ret = obj2.Substraction()
print("Substraction is :",Ret)
Ret = obj2.Multiplication()
print("Multiplication is :",Ret)
Ret = obj2.Division()
print("Division is :",Ret)
print("-------------------------------------")

print("-------------for obj1----------------")
Ret = obj3.Addition()
print("Addition is :",Ret)
Ret = obj3.Substraction()
print("Substraction is :",Ret)
Ret = obj3.Multiplication()
print("Multiplication is :",Ret)
Ret = obj3.Division()
print("Division is :",Ret)
print("-------------------------------------")