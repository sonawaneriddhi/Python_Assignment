####################################################################################################
#
# Description : Write a program which contains filter(), map() and reduce() in it.Python application 
#               which contains one list of numbers. List contains the numbers which are accepted from user.
#               Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90.
#               Map function will increase each number by 10.
#               Reduce will return product of all that numbers.
# Input       : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# Output      : List after filter :
#               [76, 89, 86, 90, 70]
#               List after map :
#               [86, 99, 96, 100, 80]
#               Output of reduce :
#               6538752000
#
######################################################################################################
import functools

def Greater(No):
    if((No >= 70) and (No <= 90)):
        return No

def AddTen(No):
    return No + 10

def Product(A,B):
    return A*B

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

    fdata = list(filter(Greater,data))
    print("List after filter :",fdata)

    mdata = list(map(AddTen,fdata))
    print("List after map :",mdata)

    Ret = functools.reduce(Product,mdata)
    print("Output of reduce :",Ret)

    
if __name__ == "__main__":
    main()