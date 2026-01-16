########################################################################################
#
# Description : Write a lambda function using filter() which accepts list of numbers 
#               and returns list of numbers that are divisible by both 3 and 5
# Input       : [15,61,73,45,30] 
# Output      : [15,45,30]
#
########################################################################################

CheckDivisible = lambda iNo : (iNo % 3 == 0 and iNo % 5 == 0)

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

    FData = list(filter(CheckDivisible , Data))

    print("Numbers that are divisible by both 3 & 5 are :",FData)
    
if __name__ == "__main__":
    main() 