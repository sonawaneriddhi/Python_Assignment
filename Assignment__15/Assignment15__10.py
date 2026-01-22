#####################################################################################
#
# Description : Write a lambda function using filter() which accepts list of numbers 
#               and returns count of all even elements
# Input       : [1,4,5,2,3] 
# Output      : 2
#
#####################################################################################

CountEven = lambda iNo : iNo % 2 == 0

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

    FData = list(filter(CountEven , Data))

    print("Count of even numbers in the list :",len(FData))

if __name__ == "__main__":
    main() 