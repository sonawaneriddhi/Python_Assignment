###################################################################################################
#
# Description : Write a program which accepts one number and print count of digits in that number 
# Input       : 7521
# Output      : 4
#
###################################################################################################

def CountDigits(iNo):
    iCount = 0

    while(iNo != 0):
        iNo = iNo // 10
        iCount = iCount + 1

    return iCount

def main():
    iValue = 0
    iRet = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = CountDigits(iValue) 

    print("Number of digits in",iValue,"is :",iRet)

if __name__ == "__main__":
    main() 