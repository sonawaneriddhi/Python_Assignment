####################################################################################################
#
# Description : Write a lambda function which accepts two numbers and returns the minimum number
# Input       : 5 , 10
# Output      : 5
#
####################################################################################################

Minimum = lambda iNo1,iNo2 : iNo1 if(iNo1 < iNo2) else iNo2

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter the first number : ", end = "")
    iValue1 = int(input())

    print("Enter the second number : ", end = "")
    iValue2 = int(input())

    iRet = Minimum(iValue1,iValue2)

    print("Minimum is :",iRet)

if __name__ == "__main__":
    main() 