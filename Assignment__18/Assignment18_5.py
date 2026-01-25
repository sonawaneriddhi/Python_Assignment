####################################################################################################
#
# Description : Accept N numbers from user and store into list.
#               Return addition of all prime numbers from list.
#               Use user-defined module MarvellousNum and function ChkPrime().
# Input       : Number of elements : 11
#               Elements : 13 5 45 7 4 56 5 34 2 5 65
# Output      : 54 (13 + 5 + 7 + 2 + 5)
#
######################################################################################################
import MarvellousNum as num

def ListPrime(Arr):
    bFlag = False
    Sum = 0

    for No in Arr:
        bFlag = num.ChkPrime(No)
        if(bFlag == True):
            Sum = Sum + No
    
    return Sum


def main():
    Data = list()
    Size = 0

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        Data.append(int(input()))

    Ret = ListPrime(Data)

    print("Sum of prime number from list is :",Ret)
    
if __name__ == "__main__":
    main()