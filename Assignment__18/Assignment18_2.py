####################################################################################################
#
# Description : Accept N numbers from user and store into list.
#               Return maximum number from list.
# Input       : Number of elements : 7
#               Elements : 13 5 45 7 4 56 34
# Output      : 56
#
######################################################################################################
def Max(Arr):
    Max = Arr[0]
    
    for No in Arr:
        if(No > Max):
            Max = No

    return Max

def main():
    Data = list()
    Size = 0

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        Data.append(int(input()))

    Ret = Max(Data)

    print("Maximum from list is :",Ret)
    
if __name__ == "__main__":
    main()