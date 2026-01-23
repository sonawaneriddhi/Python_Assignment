############################################################################################################
#
# Description : Write a program which accepts one number and prints multiplication table of that number
# Input       : 4
# Output      : 4 8 12 16 20 24 28 32 36 40 
#
############################################################################################################

def MultiplicationTable(iNo):
    iMult = 0

    for iCnt in range(1,11,1):
        iMult = iCnt * iNo
        print(iMult,end=" ")
    
    print()

def main():
    iValue = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    MultiplicationTable(iValue) 

if __name__ == "__main__":
    main() 