####################################################################################################
#
# Description : Write a program which contains one function that accept one number from user and 
#               returns True if number is divisible by 5 otherwise return False.
# Input       : 8
# Output      : False
# Input       : 25
# Output      : True
#
######################################################################################################

def CheckNum(No):
    bFlag = False

    if((No % 5) == 0):
        bFlag = True
    else:
        bFlag = False

    return bFlag

def main():
    Value = 0
    bRet = False

    Value = int(input("Enter a number : "))
    
    bRet = CheckNum(Value)

    print(bRet)

if __name__ == "__main__":
    main() 