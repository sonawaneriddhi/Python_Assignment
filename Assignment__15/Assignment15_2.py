######################################################################################
#
# Description : Write a lambda function using filter() which accepts list of numbers 
#               and returns a list of even numbers
# Input       : [1,2,3,4,5,6,7,8,9,10] 
# Output      : [2,4,6,8,10]
#
######################################################################################

CheckEven = lambda iNo : (iNo % 2 == 0)

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

    FData = list(filter(CheckEven , Data))

    print("Even numbers from the list is :",FData)

if __name__ == "__main__":
    main() 