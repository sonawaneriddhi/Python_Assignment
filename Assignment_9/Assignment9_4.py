##########################################################################################
#
# Description : Write a program which accepts one number & prints cube of that number
# Input       : 5
# Output      : 125
#
#########################################################################################

def CubeX(iNo):
    iCube = 0

    iCube = iNo * iNo * iNo

    return iCube

def main():
    iValue = 0
    iRet = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    iRet = CubeX(iValue) 

    print("The cube of",iValue,"is :",iRet)

if __name__ == "__main__":
    main() 