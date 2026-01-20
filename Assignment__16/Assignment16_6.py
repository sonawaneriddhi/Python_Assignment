####################################################################################################
#
# Description : Write a program which accept number from user and check whether that number is 
#               positive, negative or zero.
# Input       : 11
# Output      : Positive
# Input       : -8
# Output      : Negative
# Input       : 0
# Output      : Zero
#
######################################################################################################

def CheckNum(No):
    if(No > 0):
        print("Positive")
    elif(No < 0):
        print("Negative")
    else:
        print("Zero")

def main():
    Value = 0

    Value = int(input("Enter a number : "))
    
    CheckNum(Value)

if __name__ == "__main__":
    main() 