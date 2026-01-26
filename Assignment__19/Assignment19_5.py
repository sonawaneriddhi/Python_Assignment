####################################################################################################
#
# Description : Write a program which contains filter(), map() and reduce() in it.Python application 
#               which contains one list of numbers. List contains the numbers which are accepted from user.
#               Filter should filter out all prime numbers.
#               Map function will multiply each number by 2.
#               Reduce will return maximum number from that numbers.
#               (You can also use normal functions instead of lambda functions.)
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

def Prime(No):
    bFlag = True
    for i in range(2,(No // 2) + 1):
        if(No % i == 0):
            bFlag = False
            break
    
    if(bFlag == True):
        return No

def Multiply(No):
    return No * 2

def Maximum(A,B):
    if(A > B):
        return A
    else:
        return B

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

    fdata = list(filter(Prime,data))
    print("List after filter :",fdata)

    mdata = list(map(Multiply,fdata))
    print("List after map :",mdata)

    Ret = functools.reduce(Maximum,mdata)
    print("Output of reduce :",Ret)

    
if __name__ == "__main__":
    main()