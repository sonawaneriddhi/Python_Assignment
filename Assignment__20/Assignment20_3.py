####################################################################################################
#
# Description : Design a Python application that creates two threads named EvenList and OddList.
#               Both threads should accept a list of integers as input.
#               The EvenList thread should:
#                   Extract all even elements from the list.
#                   Calculate and display their sum.
#               The OddList thread should:
#                   Extract all odd elements from the list.
#                   Calculate and display their sum.
#               Threads should run concurrently.
#
######################################################################################################
import threading

def EvenList(Arr):
    Sum = 0
    evenlist = list()

    for No in Arr:
        if(No % 2 == 0):
            evenlist.append(No)
            Sum = Sum + No

    print("Sum of even elements is :",Sum)

def OddList(Arr):
    Sum = 0
    oddlist = list()

    for No in Arr:
        if(No % 2 == 1):
            oddlist.append(No)
            Sum = Sum + No

    print("Sum of odd elements is :",Sum)

def main():
    Size = 0
    data = list()
    
    Size = int(input("Enter number of elements : "))
    
    for i in range(Size):
        data.append(int(input()))   

    t1 = threading.Thread(target = EvenList,args = (data,))

    t2 = threading.Thread(target = OddList, args = (data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
    
    
if __name__ == "__main__":
    main()