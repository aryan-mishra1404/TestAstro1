def reduce_to_single_digit(number):
    while number > 9:
        number = sum(int(digit) for digit in str(number))
    return number