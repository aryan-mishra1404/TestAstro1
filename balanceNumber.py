
def calculate_balance_number(ch):

    
        if( ch == 'A' or ch == 'J' or ch == 'S'):
            return 1
        elif(ch == 'B' or ch == 'K' or ch == 'T'):
            return 2
        elif( ch == 'C' or ch == 'L' or ch == 'U'):
            return  3
        elif( ch == 'D' or ch == 'M' or ch == 'V'):
            return  4
        elif( ch == 'E' or ch == 'N' or ch == 'W'):
            return  5
        elif( ch == 'F' or ch == 'O' or ch == 'X'):
            return  6
        elif( ch == 'G' or ch == 'P' or ch == 'Y'):
            return  7
        elif( ch == 'H' or ch == 'Q' or ch == 'Z'):
            return  8
        else:
            return 9
