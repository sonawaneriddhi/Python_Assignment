######################################################################################
#
# Description : Write a lambda function using filter() which accepts list of strings 
#               and returns a list of strings with length greter than 5
# Input       : ["hello","parity","surname","name","forward"] 
# Output      : ['parity','surname','forward']
#
######################################################################################

from functools import reduce

StringLength = lambda string : (len(string) > 5)

def main():
    iSize = 0
    FData = 0

    print("Enter number of strings you want to enter : ",end = "")
    iSize = int(input())

    Data = list()

    print("Enter the strings : ")

    for iCnt in range(iSize):
        string = input()
        Data.append(string)

    FData = list(filter(StringLength, Data))

    print("Strings with size less than 5 from the list are :",FData)

if __name__ == "__main__":
    main() 