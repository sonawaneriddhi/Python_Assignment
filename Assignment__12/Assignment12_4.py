#######################################################################################################
#
# Description : Write a program which accepts one number and prints that many numbers starting from 1
# Input       : 5
# Output      : 1 2 3 4 5
#
#######################################################################################################

def Display(iNo):
    for iCnt in range(1,iNo + 1):
        print(iCnt, end = " ")

    print()

def main():
    iValue = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main() 