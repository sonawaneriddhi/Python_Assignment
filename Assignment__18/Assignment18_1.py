####################################################################################################
#
# Description : Accept N numbers from user and store into list.
#               Return addition of all elements.
# Input       : Number of elements : 6
#               Elements : 13 5 45 7 4 56
# Output      : 130
#
######################################################################################################
def SumList(Arr):
    Sum = 0
    
    for No in Arr:
        Sum = Sum + No

    return Sum

def main():
    Data = list()
    Size = 0

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        Data.append(int(input()))

    Ret = SumList(Data)

    print("Sum of numbers in list are :",Ret)
    
if __name__ == "__main__":
    main()