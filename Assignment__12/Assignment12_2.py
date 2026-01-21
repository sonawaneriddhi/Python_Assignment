###################################################################################
#
# Description : Write a program which accepts one number and prints its factors
# Input       : 12
# Output      : 1 2 3 4 6 12 
#
###################################################################################

def DisplayFactors(iNo):

    print("Factors are : ")

    for iCnt in range(1,iNo + 1):
        if(iNo % iCnt == 0):
            print(iCnt,end = " ")

    print()

def main():
    iValue = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    DisplayFactors(iValue) 

if __name__ == "__main__":
    main() 