####################################################################################################
#
# Description : Write a program which accept one number from user and check whether number 
#               is prime or not.
# Input       : 5
# Output      : Prime Number
# Input       : 10
# Output      : Not a Prime Number
#
######################################################################################################
def ChkPrime(No):
    bFlag = True

    for i in range(2,(No // 2) + 1):
        if((No % i) == 0):
            bFlag = False
            break
        
    return bFlag

def main():
    Value = 0
    bRet = 0

    Value = int(input("Enter a number : "))
    
    bRet = ChkPrime(Value)

    if(bRet == True):
        print("Prime Number")
    else:
        print("Not a Prime Number")
        
if __name__ == "__main__":
    main()