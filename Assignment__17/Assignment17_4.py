####################################################################################################
#
# Description : Write a program which accept one number from user and return addition of its factors.
# Input       : 12
# Output      : 16 (1 + 2 + 3 + 4 + 6)
#
######################################################################################################
def AddFactors(No):
    Sum = 0

    for i in range(1,(No // 2) + 1):
        if((No % i) == 0):
            Sum = Sum + i

    return Sum

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter a number : "))
    
    Ret = AddFactors(Value)

    print("Sum of factors is :",Ret)
    
if __name__ == "__main__":
    main()