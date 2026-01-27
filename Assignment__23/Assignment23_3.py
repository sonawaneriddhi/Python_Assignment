###########################################################################################3######
# Description : Write a Python program to implement a class named Numbers with the 
#               following specifications:
#               The class should contain one instance variable:
#                   Value
#               Define a constructor (__init__) that accepts a number from the user and 
#               initializes Value.
#               Implement the following instance methods:
#                   ChkPrime() – returns True if the number is prime, otherwise returns False
#                   ChkPerfect() – returns True if the number is perfect, otherwise returns False
#                   Factors() – displays all factors of the number
#                   SumFactors() – returns the sum of all factors
#                   (You may use this method as a helper in ChkPerfect() if required)
#               Create multiple objects and call all methods.
#
###################################################################################################
class Numbers:
    def __init__(self, No):
        self.Value = No

    def ChkPrime(self):
        bFlag = True

        if self.Value <= 1:
            return False

        for i in range(2, (self.Value // 2) + 1):
            if self.Value % i == 0:
                bFlag = False
                break
        return bFlag

    def Factors(self):
        print("Factors of",self.Value,"are:")

        for i in range(1, (self.Value + 1)):
            if self.Value % i == 0:
                print(i, end=" ")

        print()

    def SumFactors(self):
        Sum = 0
        for i in range(1, (self.Value + 1)):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum

    def ChkPerfect(self):
        bRet = False

        if((self.SumFactors() - self.Value) == self.Value):
            bRet = True
        else:
            bRet = False

        return bRet

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))

    obj1 = Numbers(No1)
    obj2 = Numbers(No2)

    print("Number :",obj1.Value)
    print("Prime :", obj1.ChkPrime())
    print("Perfect :", obj1.ChkPerfect())
    obj1.Factors()
    print("Sum of factors:", obj1.SumFactors())

    print("Number:",obj2.Value)
    print("Prime :", obj2.ChkPrime())
    print("Perfect :", obj2.ChkPerfect())
    obj2.Factors()
    print("Sum of factors :", obj2.SumFactors())

if __name__ == "__main__":
    main()
