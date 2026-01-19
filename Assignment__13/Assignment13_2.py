###########################################################################################
#
# Description : Write a program which accepts radius of circle and prints area of circle
# Input       : 5
# Output      : 78.53981633974483
#
###########################################################################################

import math

def CalculateAreaOfCircle(iRadius):
    iArea = 0
    iArea = (math.pi) * (iRadius ** 2)
    return iArea

def main():
    iRadius = 0
    iRet = 0

    print("Enter radius : ",end = "")
    iRadius = int(input())

    iRet = CalculateAreaOfCircle(iRadius)

    print("Area of Circle is :",iRet)

if __name__ == "__main__":
    main() 