####################################################################################################
#
# Description : Write a program which accept number from user and return number of digits.
# Input       : 5187934
# Output      : 7
#
######################################################################################################
def CountDigits(No):
    Count = 0

    while(No != 0):
        No = No // 10
        Count = Count + 1

    return Count

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter a number : "))
    
    Ret = CountDigits(Value)

    print("Digits are :",Ret)
    
if __name__ == "__main__":
    main()