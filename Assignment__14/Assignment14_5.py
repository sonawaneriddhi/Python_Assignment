#######################################################################################################################
#
# Description : Write a lambda function which accepts one number and returns True if number is even otherwise False
# Input       : 5 
# Output      : False
#
#######################################################################################################################

ChkEven = lambda iNo : (iNo % 2 == 0)

def main():
    iValue = 0
    bRet = False

    print("Enter the number : ",end = "")
    iValue = int(input())

    bRet = ChkEven(iValue)

    print(bRet)

if __name__ == "__main__":
    main() 