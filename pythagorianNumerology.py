
def getDreamNumber(nameList):

    hn =0
    for ch in nameList:
        if(ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            print("")
        else:
            if( ch == 'J' or ch == 'S'):
                hn += 1
            elif( ch == 'B' or ch == 'K' or ch == 'T'):
                hn +=2
            elif( ch == 'C' or ch == 'L'):
                hn += 3
            elif( ch == 'D' or ch == 'M' or ch == 'V'):
                hn += 4
            elif( ch == 'N' or ch == 'W'):
                hn += 5
            elif( ch == 'F' or ch == 'X'):
                hn += 6
            elif( ch == 'G' or ch == 'P' or ch == 'Y'):
                hn += 7
            elif( ch == 'H' or ch == 'Q' or ch == 'Z'):
                hn += 8
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
        if( ch == 'A' or ch == 'J' or ch == 'S'):
            dn += 1
        elif(ch == 'B' or ch == 'K' or ch == 'T'):
            dn +=2
        elif( ch == 'C' or ch == 'L' or ch == 'U'):
            dn += 3
        elif( ch == 'D' or ch == 'M' or ch == 'V'):
            dn += 4
        elif( ch == 'E' or ch == 'N' or ch == 'W'):
            dn += 5
        elif( ch == 'F' or ch == 'O' or ch == 'X'):
            dn += 6
        elif( ch == 'G' or ch == 'P' or ch == 'Y'):
            dn += 7
        elif( ch == 'H' or ch == 'Q' or ch == 'Z'):
            dn += 8
        else:
            dn+=9
    if(dn == 11 or dn ==22):
        return dn
    num1 = dn%10
    num2 = int( dn/10)
    dn = num1+num2
    return dn