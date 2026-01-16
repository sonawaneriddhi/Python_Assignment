#####################################################################################
#
# Description : Write a lambda function using filter() which accepts list of numbers 
#               and returns a list of odd numbers
# Input       : [1,2,3,4,5,6,7,8,9,10] 
# Output      : [1,3,5,7,9]
#
#####################################################################################

CheckOdd = lambda iNo : (iNo % 2 != 0)

def main():
    iSize = 0
    iValue = 0
    FData = 0

    print("Enter number of elements : ",end = "")
    iSize = int(input())

    Data = list()

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        Data.append(iValue)

    FData = list(filter(CheckOdd , Data))

    print("Odd numbers from the list is:",FData)

if __name__ == "__main__":
    main() 