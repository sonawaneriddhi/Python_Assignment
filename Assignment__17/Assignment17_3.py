####################################################################################################
#
# Description : Write a program which accept one number from user and return its factorial.
# Input       : 5
# Output      : 120
#
######################################################################################################
def Fact(No):
    Fact = 1

    for i in range(No,1,-1):
        Fact = Fact * i

    return Fact

def main():
    Value = 0
    Ret = 0

    Value = int(input("Enter a number : "))
    
    Ret = Fact(Value)

    print("Sum of factors is :",Ret)
    
if __name__ == "__main__":
    main()