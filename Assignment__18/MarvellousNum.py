def ChkPrime(No):
    bFlag = True
    
    for i in range(2,(No // 2) + 1):
        if((No % i) == 0):
            bFlag = False
            break

    return bFlag
