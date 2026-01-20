######################################################################################
#
# Description : Write a lambda function which accepts 2 numbers and returns addition 
# Input       : 5 ,10
# Output      : 15
#
######################################################################################

Addition = lambda iNo1 , iNo2 : iNo1 + iNo2

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter first number : ", end = "")
    iValue1 = int(input())

    print("Enter second number : ", end = "")
    iValue2 = int(input())

    iRet = Addition(iValue1,iValue2)

    print("Addition is :",iRet)

if __name__ == "__main__":
    main() 