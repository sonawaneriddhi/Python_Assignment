###############################################################################################
#
# Description : Write a program which accepts length and width of a rectangle and prints area
# Input       : 5 , 10
# Output      : Area : 50 
#
###############################################################################################

def CalculateAreaOfRectangle(iLength , iWidth):
    iArea = 0
    iArea = iLength * iWidth
    return iArea

def main():
    iLength = 0
    iWidth = 0
    iRet = 0

    print("Enter length : ",end = "")
    iLength = int(input())

    print("Enter width : ",end = "")
    iWidth = int(input())

    iRet = CalculateAreaOfRectangle(iLength, iWidth)

    print("Area of Rectangle is :",iRet)

if __name__ == "__main__":
    main() 