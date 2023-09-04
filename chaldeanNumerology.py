
def getDreamNumber(nameList):

    hn =0
    for ch in nameList:
        if(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            print("")
        else:
            if( ch == 'J' or ch == 'Q' or ch == 'Y'):
                hn += 1
            elif( ch == 'B' or ch == 'K' or ch == 'R'):
                hn +=2
            elif( ch == 'C' or ch == 'G' or ch == 'L' or ch == 'S'):
                hn += 3
            elif( ch == 'D' or ch == 'M' or ch == 'T'):
                hn += 4
            elif( ch == 'H' or ch == 'N' or ch == 'X'):
                hn += 5
            elif( ch == 'V' or ch == 'W'):
                hn += 6
            elif(ch == 'Z'):
                hn += 7
            else:
                hn+=8
    if(hn == 11 or hn ==22):
        return hn
    num1 = hn%10
    num2 = (int( hn/10))
    hn = num1+num2
    return hn


def getSoulNumber(nameList):
    sn =0
    for ch in nameList:
        if (ch == 'A' or ch == 'I'):
            sn += 1
        if (ch == 'E'):
            sn += 5
        if (ch == 'U'):
            sn += 6
        if (ch == 'O'):
            sn += 7
    if(sn == 11 or sn ==22):
        return sn
    num1 = sn%10
    num2 = (int( sn/10))
    sn = num1+num2
    return sn



def getDestinyNumber(nameList):

    dn =0
    for ch in nameList:
        if( ch == 'A' or ch == 'I' or ch == 'J' or ch == 'Q' or ch == 'Y'):
            dn += 1
        elif(ch == 'B' or ch == 'K' or ch == 'R'):
            dn +=2
        elif( ch == 'C' or ch == 'G' or ch == 'L' or ch == 'S'):
            dn += 3
        elif( ch == 'D' or ch == 'M' or ch == 'T'):
            dn += 4
        elif( ch == 'E' or ch == 'H' or ch == 'N' or ch == 'X'):
            dn += 5
        elif( ch == 'U' or ch == 'V' or ch == 'W'):
            dn += 6
        elif( ch == 'O' or ch == 'Z'):
            dn += 7
        else:
            dn+=8
    if(dn == 11 or dn ==22):
        return dn
    num1 = dn%10
    num2 = (int( dn/10))
    dn = num1+num2
    return dn