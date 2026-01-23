#####################################################################################################
#
# Description : Write a program which accepts one number and checks whether it is palindrome or not
# Input       : 121
# Output      : Palindrome
#
#####################################################################################################

def CheckPalindrome(iNo):
    iDigit = 0
    iReverse = 0
    iTemp = iNo
    bFlag = False

    while(iNo != 0):
        iDigit = iNo % 10
        iReverse = iReverse * 10 + iDigit
        iNo = iNo // 10

    if(iTemp == iReverse):
        bFlag = True

    return bFlag

def main():
    iValue = 0
    bRet = False

    print("Enter number : ",end = "")
    iValue = int(input())

    bRet = CheckPalindrome(iValue) 

    if(bRet == True):
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main() 