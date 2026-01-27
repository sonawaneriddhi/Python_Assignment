####################################################################################################
#
# Description : Design a Python application that creates two threads.
#               Thread 1 should calculate and display the maximum element from a list.
#               Thread 2 should calculate and display the minimum element from the same list.
#               The list should be accepted from the user.
#
######################################################################################################
import threading

def Maximum(Arr):
    Max = Arr[0]

    for No in Arr:
        if(No > Max):
            Max = No
        
    print("Maximum is :",Max)

def Minimum(Arr):
    Min = Arr[0]

    for No in Arr:
        if(No < Min):
            Min = No
        
    print("Minimum is :",Min)

def main():
    Size = 0
    data = list()
    
    Size = int(input("Enter number of elements : "))
    
    for i in range(Size):
        data.append(int(input()))   

    t1 = threading.Thread(target = Maximum,args = (data,))

    t2 = threading.Thread(target = Minimum, args = (data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
    
if __name__ == "__main__":
    main()