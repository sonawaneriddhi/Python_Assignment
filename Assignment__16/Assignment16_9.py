####################################################################################################
#
# Description : Write a program which display first 10 even numbers on screen.
# Input       : Nothing
# Output      : 2   4   6   8   10  12  14  16  18  20
#
######################################################################################################

def Display(No):
    for i in range(2,((No * 2) + 1),2):
        print(i,end = " ")

    print()

def main():
    Display(10)

if __name__ == "__main__":
    main() 