####################################################################################################
#
# Description : Write a program which accept one number and display below pattern.
# Input       : 3
# Output      : *
#               * *
#               * * *
#
######################################################################################################
def Display(No):
    for i in range(No):
        for j in range(i,No):
            print("*", end = " ")
        print()

    print()

def main():
    Value = 0

    Value = int(input("Enter a number : "))
    
    Display(Value)
    
if __name__ == "__main__":
    main()