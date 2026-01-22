#####################################################################################
#
# Description : Write a lambda function using reduce() which accepts list of numbers 
#               and returns product of all elements
# Input       : [1,2,3,4,5] 
# Output      : 120
#
#####################################################################################

from functools import reduce

Product = lambda iNo1,iNo2 : iNo1 * iNo2

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

    RData = reduce(Product , Data)

    print("Product of all elements is :",RData)

if __name__ == "__main__":
    main() 