####################################################################################################
#
# Description : Write a program which accept number from user and print that number of "*" on screen.
# Input       : 5
# Output      : * * * * *
#
######################################################################################################

def Display(No):
    for i in range(No):
        print("*",end = " ")

    print()

def main():
    Value = 0

    Value = int(input("Enter a number : "))
    
    Display(Value)

if __name__ == "__main__":
    main() 