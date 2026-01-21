##########################################################################################################################
#
# Description : Write a program which accepts two numbers and prints addition, substraction, multiplication and division
# Input       : 11, 10
# Output      : Addition : 21
#               Subtraction : 1
#               Multiplication : 110
#               Division : 1.1
#
##########################################################################################################################

def Addition(iNo1,iNo2):
    iAns = 0
    iAns = iNo1 + iNo2
    return iAns

def Subtraction(iNo1,iNo2):
    iAns = 0
    iAns = iNo1 - iNo2
    return iAns

def Multiplication(iNo1,iNo2):
    iAns = 0
    iAns = iNo1 * iNo2
    return iAns

def Division(iNo1,iNo2):
    iAns = 0

    try:
        iAns = iNo1 / iNo2

    except ZeroDivisionError as zobj:
        print("Exception :",zobj)

    return iAns

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter the first number : ",end = "")
    iValue1 = int(input())

    print("Enter the second number : ",end = "")
    iValue2 = int(input())

    iRet = Addition(iValue1, iValue2) 
    print("Addition is :",iRet)

    iRet = Subtraction(iValue1, iValue2) 
    print("Subtraction is :",iRet)

    iRet = Multiplication(iValue1, iValue2) 
    print("Multiplication is :",iRet)

    iRet = Division(iValue1, iValue2) 
    print("Division is :",iRet)

if __name__ == "__main__":
    main() 