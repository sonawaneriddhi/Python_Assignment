####################################################################################################
#
# Description : Accept N numbers from user and store into list.
#               Accept one number and return its frequency from list.
# Input       : Number of elements : 11
#               Elements : 13 5 45 7 4 56 5 34 2 5 65
#               Enter a number to check frequency : 5
# Output      : 3
#
######################################################################################################
def Frequency(Arr,Num):
    Count = 0

    for No in Arr:
        if(No == Num):
            Count = Count + 1

    return Count

def main():
    Data = list()
    Size = 0
    Value = 0

    Size = int(input("Enter number of elements : "))

    for i in range(Size):
        Data.append(int(input()))

    Value = int(input("Enter a number to check frequency : "))

    Ret = Frequency(Data,Value)

    print("Minimum from list is :",Ret)
    
if __name__ == "__main__":
    main()