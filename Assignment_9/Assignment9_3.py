##########################################################################################
#
# Description : Write a program which accepts one number and prints square of that number
# Input       : 5
# Output      : 25
#
###########################################################################################

def SquareX(iNo):
    iSquare = 0

    iSquare = iNo * iNo

    return iSquare

def main():
    iValue = 0
    iRet = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    iRet = SquareX(iValue) 

    print("The square of",iValue,"is :",iRet)

if __name__ == "__main__":
    main() 