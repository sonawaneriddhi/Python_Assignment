######################################################################################################
#
# Description : Write a program which accepts one character and checks whether is vowel or consonant
# Input       : a
# Output      : Vowel
#
######################################################################################################

def ChkVowel(cCh):
    bFlag = False

    if((cCh == 'a') or (cCh == 'e') or (cCh == 'i') or (cCh == 'o') or (cCh == 'u') or (cCh == 'A') or (cCh == 'E') or (cCh == 'I') or (cCh == 'O') or (cCh == 'U')):
        bFlag = True

    return bFlag

def main():
    cChar = '\0'
    bRet = False

    print("Enter the character : ",end = "")
    cChar = input()

    bRet = ChkVowel(cChar) 

    if(bRet == True):
        print("Vowel")
    else:
        print("Consonant")

if __name__ == "__main__":
    main() 