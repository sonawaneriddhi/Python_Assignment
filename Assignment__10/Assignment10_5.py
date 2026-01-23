###################################################################################################
#
# Description : Write a program which accepts one number and prints all odd numbers till that number
# Input       : 11
# Output      : 1 3 5 7 9 11
#
###################################################################################################

def PrintOdd(iNo):

    for iCnt in range(1,iNo+1):
        if(iCnt % 2 != 0):
            print(iCnt,end = " ")

    print()
    
def main():
    iValue = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    PrintOdd(iValue) 

if __name__ == "__main__":
    main() 