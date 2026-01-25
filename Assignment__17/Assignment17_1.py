####################################################################################################
#
# Description : Create one module named Arithmetic which contains 4 functions:
#               Add() for addition
#               Sub() for subtraction
#               Mult() for multiplication
#               Div() for division
#               All functions accept two parameters.
#               Write a Python program which calls all functions from Arithmetic module.
# Input       : 10
#               11
# Output      : Addition is : 21
#               Subtraction is : -1
#               Multiplication is : 110
#               Division is : 0.9090909090909091
#
######################################################################################################
import Assignment17_1Module as mathss

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    
    Ret = mathss.Addition(Value1,Value2)
    print("Addition is :",Ret)

    Ret = mathss.Subtraction(Value1,Value2)
    print("Subtraction is :",Ret)

    Ret = mathss.Multiplication(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = mathss.Division(Value1,Value2)
    print("Division is :",Ret)

if __name__ == "__main__":
    main()