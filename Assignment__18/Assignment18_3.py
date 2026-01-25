####################################################################################################
#
# Description : Accept N numbers from user and store into list.
#               Return minimum number from list.
# Input       : Number of elements : 4
#               Elements : 13 5 45 7
# Output      : 5
#
######################################################################################################
def Min(Arr):
    Min = Arr[0]
    
    for No in Arr:
        if(No < Min):
            Min = No

    return Min

def main():
    Data = list()
    Size = 0

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        Data.append(int(input()))

    Ret = Min(Data)

    print("Minimum from list is :",Ret)
    
if __name__ == "__main__":
    main()