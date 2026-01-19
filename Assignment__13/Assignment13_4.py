####################################################################################
#
# Description : Write a program which accepts one number & prints binary equivalent
# Input       : 10
# output      : 1010
#
###################################################################################

def DisplayBinary(iNo):
    iDigit = 0
    binary = list()

    while(iNo != 0):
        iDigit = iNo % 2
        binary.append(str(iDigit))
        iNo = iNo // 2

    print("Binary Equivalent :",end = " ")
    print("".join(binary[::-1]))

def main():
    iValue = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    DisplayBinary(iValue)

if __name__ == "__main__":
    main() 