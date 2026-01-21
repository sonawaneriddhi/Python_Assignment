######################################################################################################
#
# Description : Write a program which accepts one number and prints that many numbers in reverse order
# Input       : 5
# Output      : 5 4 3 2 1 
#
######################################################################################################

def Display(iNo):
    for iCnt in range(iNo , 0 , -1):
        print(iCnt, end = " ")

    print()

def main():
    iValue = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main() 