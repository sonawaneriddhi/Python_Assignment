#######################################################################################
#
# Description : Write a lambda function using map() which accepts list of numbers and 
#               returns a list of squares of each number 
# Input       : [1,2,3,4,5] 
# Output      : [1,4,9,16,25]
#
########################################################################################

Square = lambda iNo : (iNo * iNo)

def main():
    iSize = 0
    iValue = 0
    MData = 0

    print("Enter number of elements : ", end ="")
    iSize = int(input())

    Data = list()

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        Data.append(iValue)

    MData = list(map(Square, Data))

    print("Squares of all numbers from the list is :",MData)

if __name__ == "__main__":
    main() 