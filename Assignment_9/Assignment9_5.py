#########################################################################################################
#
# Description : Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input       : 15
# Output      : Divisible by 3 & 5
#
########################################################################################################

def CheckDivisible(iNo):
    bFlag = False

    if((iNo % 3 == 0) and (iNo % 5 == 0)):
        bFlag = True
    
    return bFlag

def main():
    iValue = 0
    bRet = False

    print("Enter the number : ",end = "")
    iValue = int(input())

    bRet = CheckDivisible(iValue) 

    if(bRet == True):
        print(iValue,"is divisible by 3 & 5")
    else:
        print(iValue,"is not divisible 3 & 5")

if __name__ == "__main__":
    main() 
