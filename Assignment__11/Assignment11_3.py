##################################################################################
#
# Description : Write a program which accepts one number and prints sum of digits
# Input       : 123
# Output      : 6
#
##################################################################################

def SumDigits(iNo):
    iDigit = 0
    iSum = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo // 10

    return iSum

def main():
    iValue = 0
    iRet = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = SumDigits(iValue) 

    print("Sum of digits is :",iRet)

if __name__ == "__main__":
    main() 