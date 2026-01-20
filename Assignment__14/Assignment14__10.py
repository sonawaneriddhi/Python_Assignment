#################################################################################################
#
# Description : Write a lambda function which accepts three numbers and returns Largest number
# Input       : 5 , 20 , 10
# Output      : 20
#
#################################################################################################

LargestNumber = lambda iNo1 , iNo2 , iNo3 : iNo1 if(iNo1 > iNo2 and iNo1 > iNo3) else(iNo2 if(iNo2 > iNo1 and iNo2 > iNo3) else iNo3)

def main():
    iValue1 = 0
    iValue2 = 0
    iValue3 = 0
    iRet = 0

    print("Enter first number : ",end = "")
    iValue1 = int(input())

    print("Enter second number : ", end = "")
    iValue2 = int(input())

    print("Enter third number : ", end = "")
    iValue3 = int(input())

    iRet = LargestNumber(iValue1 , iValue2,iValue3)

    print("Largest number is :",iRet)

if __name__ == "__main__":
    main() 