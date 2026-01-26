####################################################################################################
#
# Description : Design a Python application that creates three threads named Small, Capital, and Digits.
#               All threads should accept a string as input.
#               The Small thread should:
#                   Count and display the number of lowercase characters.
#               The Capital thread should:
#                   Count and display the number of uppercase characters.
#               The Digits thread should:
#                   Count and display the number of numeric digits.
#               Each thread must also display:
#                   Thread ID
#                   Thread Name
#
######################################################################################################
import threading

def CapitalLetters(string):
    t1 = threading.current_thread()
    print("Thread ID :",t1.ident)
    print("Thread Name :",t1.name)
    Count = 0
    for let in string:
        ascii = ord(let)
        if 65 <= ascii <= 90:
            Count = Count + 1

    print("Count of Capital Letters :",Count)

def SmallLetters(string):
    t1 = threading.current_thread()
    print("Thread ID :",t1.ident)
    print("Thread Name :",t1.name)
    Count = 0
    for let in string:
        ascii = ord(let)
        if 97 <= ascii <= 122:
            Count = Count + 1

    print("Count of Small letters:",Count)

def Digit(string):
    t1 = threading.current_thread()
    print("Thread ID :",t1.ident)
    print("Thread Name :",t1.name)
    Count = 0
    for let in string:
        ascii = ord(let)
        if 48 <= ascii <= 57:
            Count = Count + 1

    print("Count of dgitis :",Count)

def main():
    Value = 0
    
    Value = input("Enter a string : ")
    
    Small = threading.Thread(target = SmallLetters,args = (Value,))

    Capital = threading.Thread(target = CapitalLetters, args = (Value,))

    Digits = threading.Thread(target = Digit, args = (Value,))

    Small.start()
    Capital.start()
    Digits.start()
    
    Small.join()
    Capital.join()
    Digits.join()

    print("Exit from main")
    
    
if __name__ == "__main__":
    main()