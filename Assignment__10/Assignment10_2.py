######################################################################################################
#
# Description : Write a program which accepts one number and prints sum of first N natural numbers
# Input       : 5
# Output      : 15
#
######################################################################################################

def SumNatural(iNo):
    iSum = 0

    for iCnt in range(iNo+1):
        iSum = iSum + iCnt
        
    return iSum

def main():
    iValue = 0
    iRet = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = SumNatural(iValue) 

    print("The sum of first N natural numbers is :",iRet)

if __name__ == "__main__":
    main() 