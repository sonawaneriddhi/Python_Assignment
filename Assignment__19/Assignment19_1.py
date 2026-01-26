####################################################################################################
#
# Description : Write a program which contains one lambda function which accepts one parameter 
#               and return power of two.
# Input       : 4
# Output      : 16
# Input       : 6
# Output      : 64
#
######################################################################################################
Power = lambda No : No ** 2

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter a number : "))

    Ret = Power(Value)

    print("Power is :",Ret)
    
if __name__ == "__main__":
    main()