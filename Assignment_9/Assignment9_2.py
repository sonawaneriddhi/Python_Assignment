####################################################################
#
# Description : Write a program which contains one function ChkGreater() that accepts 
#               two numbers and print the greater number.
# Input       : 10 20 
# Output      : 20 is greater
#
####################################################################

def ChkGreater(iNo1,iNo2):
    iGreater = 0

    if(iNo1 > iNo2):
        iGreater = iNo1
    else:
        iGreater = iNo2

    return iGreater

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter the first number : ",end = "")
    iValue1 = int(input())

    print("Enter the second number : ",end = "")
    iValue2 = int(input())

    iRet = ChkGreater(iValue1,iValue2) 

    print(iRet,"is greater")

if __name__ == "__main__":
    main() 