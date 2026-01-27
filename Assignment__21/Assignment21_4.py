####################################################################################################
#
# Description : Design a Python application that creates two threads.
#               Thread 1 should compute the sum of elements from a list.
#               Thread 2 should compute the product of elements from the same list.
#               Return the results to the main thread and display them.
#
######################################################################################################
import threading
import queue

def Summation(Arr, q):
    Sum = 0
    
    for No in Arr:
        Sum = Sum + No

    q.put(("Summation :", Sum))

def Product(Arr, q):
    Prod = 1

    for No in Arr:
        Prod = Prod * No

    q.put(("Product :", Prod))

def main():
    data = []
    q = queue.Queue()

    Size = int(input("Enter number of elements: "))

    for i in range(Size):
        data.append(int(input()))

    t1 = threading.Thread(target = Summation, args = (data, q,))

    t2 = threading.Thread(target = Product, args = (data, q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    while not q.empty():
        show, result = q.get()
        print(show, result)

    print("Exit from main")

if __name__ == "__main__":
    main()
