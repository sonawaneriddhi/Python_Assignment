####################################################################################################
#
# Description : Write a program which accept number from user and return addition of digits.
# Input       : 5187934
# Output      : 37
#
######################################################################################################
def SumDigits(No):
    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        No = No // 10
        Sum = Sum + Digit

    return Sum

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter a number : "))
    
    Ret = SumDigits(Value)

    print("Sum of Digits are :",Ret)
    
if __name__ == "__main__":
    main()