#######################################################################################################
#
# Description : Write a lambda function which accepts one number and returns square of that number
# Input       : 5 
# Output      : 25
#
#######################################################################################################

Square = lambda iNo : iNo * iNo

def main():
    iValue = 0
    iRet = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = Square(iValue)

    print("Square of",iValue,"is :",iRet)

if __name__ == "__main__":
    main() 