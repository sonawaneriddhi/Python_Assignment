############################################################################################
#
# Description : Write a program which accepts one number and prints reverse of that number
# Input       : 123
# Output      : 321
#
############################################################################################

def ReverseNumber(iNo):
    iDigit = 0
    iRev = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iRev = iRev * 10 + iDigit
        iNo = iNo // 10

    return iRev

def main():
    iValue = 0
    iRet = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = ReverseNumber(iValue) 

    print("Reverse of",iValue,"is :",iRet)

if __name__ == "__main__":
    main() 