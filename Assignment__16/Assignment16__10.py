####################################################################################################
#
# Description : Write a program which accept name from user and display length of its name.
# Input       : Marvellous
# Output      : 10
#
######################################################################################################

def StrlenX(str):
    Ret = 0
    Ret = len(str)
    return Ret 

def main():
    Value = ""
    Ret = 0

    Value = input("Enter your name : ")
    
    Ret = StrlenX(Value)

    print("Length of string :",Ret)

if __name__ == "__main__":
    main() 