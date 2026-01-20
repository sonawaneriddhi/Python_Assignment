########################################################################################################
#
# Description : Write a lambda function which accepts one number and returns True if divisible by 5
# Input       : 5 
# Output      : True
#
########################################################################################################

ChkDivisible = lambda iNo : (iNo % 5 == 0)

def main():
    iValue = 0
    bRet = 0

    print("Enter the number : ", end = "")
    iValue = int(input())

    bRet = ChkDivisible(iValue)

    print(bRet)

if __name__ == "__main__":
    main() 