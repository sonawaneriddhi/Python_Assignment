####################################################################################################
#
# Description : Write a program which contains filter(), map() and reduce() in it.Python application 
#               which contains one list of numbers. List contains the numbers which are accepted from user.
#               Filter should filter out all such numbers which are even.
#               Map function will calculate its square.
#               Reduce will return addition of all that numbers.
# Input       : [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# Output      : List after filter :
#               [2, 4, 4, 2, 8, 10]
#               List after map :
#               [4, 16, 16, 4, 64, 100]
#               Output of reduce :
#               204
#
######################################################################################################
import functools

def Even(No):
    if(No % 2 == 0):
        return No

def Square(No):
    return No*No

def Sum(A,B):
    return A + B

def main():
    data = list()
    Size = 0
    Value = 0
    Ret = 0

    Size = int(input("Enter number of elements : "))

    print("Enter the elements :")
    for i in range(Size):
        data.append(int(input()))

    print("Input list :",data)

    fdata = list(filter(Even,data))
    print("List after filter :",fdata)

    mdata = list(map(Square,fdata))
    print("List after map :",mdata)

    Ret = functools.reduce(Sum,mdata)
    print("Output of reduce :",Ret)

    
if __name__ == "__main__":
    main()