########################################################################################################
#
# Description : Write a program which accepts one number and checks whether that number is prime or not
# Input       : 11
# Output      : Prime Number
#
########################################################################################################

def ChkPrime(iNo):
    bFlag = True

    for iCnt in range(2,(iNo // 2) + 1):
        if(iNo % iCnt == 0):
            bFlag = False
            break
    
    return bFlag

def main():
    iValue = 0
    bRet = False

    print("Enter the number : ",end = "")
    iValue = int(input())

    bRet = ChkPrime(iValue) 

    if(bRet == True):
        print("Prime Number")
    else:
        print("Not a prime Number")

if __name__ == "__main__":
    main() 