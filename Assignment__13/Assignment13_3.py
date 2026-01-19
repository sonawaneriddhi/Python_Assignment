###################################################################################################################
#
# Description : Write a program which accepts one number and checks whether the number is a perfect number or not
# Input       : 6
# Output      : Perfect Number
#
###################################################################################################################

def CheckPerfect(iNo):
    iSum = 0
    bFlag = False

    for iCnt in range(1 ,(iNo // 2) + 1):
        if(iNo % iCnt == 0):
            iSum = iSum + iCnt
    
    if(iSum == iNo):
        bFlag = True
    
    return bFlag

def main():
    iValue = 0
    bRet = True

    print("Enter number : ",end = "")
    iValue = int(input())

    bRet = CheckPerfect(iValue)

    if(bRet == True):
        print("Perfect Number")
    else : 
        print("Not a Perfect Number")

if __name__ == "__main__":
    main() 