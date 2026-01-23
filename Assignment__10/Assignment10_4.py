#######################################################################################################
#
# Description : Write a program which accepts one number and prints all even numbers till that number
# Input       : 10
# Output      : 2 4 6 8 10
#
#######################################################################################################

def PrintEven(iNo):

    for iCnt in range(1,iNo+1):
        if(iCnt % 2 == 0):
            print(iCnt,end = " ")
     
    print()
    
def main():
    iValue = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    PrintEven(iValue) 

if __name__ == "__main__":
    main() 