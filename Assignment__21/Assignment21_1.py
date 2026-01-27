####################################################################################################
#
# Description : Design a Python application that creates two threads named Prime and NonPrime.
#               Both threads should accept a list of integers.
#               The Prime thread should display all prime numbers from the list.
#               The NonPrime thread should display all non-prime numbers from the list.
#
######################################################################################################
import threading

def Prime(Arr):
    bFlag = False

    for No in Arr:
        bFlag = True
        for i in range(2,(No // 2) + 1):
            if(No % i == 0):
                bFlag = False
                break
        
        if(bFlag == True):
            print("Prime :",No)

def NonPrime(Arr):
    bFlag = False

    for No in Arr:
        bFlag = True
        for i in range(2,(No // 2) + 1):
            if(No % i == 0):
                bFlag = False
                break
        
        if(bFlag == False):
            print("Non-Prime :",No)

def main():
    Size = 0
    data = list()
    
    Size = int(input("Enter number of elements : "))
    
    for i in range(Size):
        data.append(int(input()))   

    t1 = threading.Thread(target = Prime,args = (data,))

    t2 = threading.Thread(target = NonPrime, args = (data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")
    
if __name__ == "__main__":
    main()