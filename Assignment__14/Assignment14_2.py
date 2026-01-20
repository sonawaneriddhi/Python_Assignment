####################################################################################################
#
# Description : Write a lambda function which accepts one number and returns cube of that number
# Input       : 5 
# Output      : 125
#
####################################################################################################

Cube = lambda iNo : iNo * iNo * iNo

def main():
    iValue = 0
    iRet = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = Cube(iValue)

    print("Cube of",iValue,"is :",iRet)

if __name__ == "__main__":
    main() 