####################################################################################
#
# Description : Write a lambda function using reduce() which accepts list of numbers 
#               and returns minimum element
# Input       : [1,4,5,2,3] 
# Output      : 1
#
####################################################################################

from functools import reduce

CheckMinimum = lambda iNo1,iNo2 : iNo1 if iNo1 < iNo2 else iNo2

def main():
    iSize = 0
    iValue = 0
    RData = 0

    print("Enter number of elements : ",end = "")
    iSize = int(input())

    Data = list()

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        Data.append(iValue)

    RData = reduce(CheckMinimum , Data)

    print("Minimun of all elements is :",RData)

if __name__ == "__main__":
    main() 