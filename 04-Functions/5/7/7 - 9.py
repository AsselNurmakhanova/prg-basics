def f(number, even):
    number = str(number)
    total = 0
    if even == True:
        for char in number:
            digit = int(char)
            if digit % 2 == 0:
                total += digit
    elif even == False:
        for char in number:
            digit = int(char)
            if digit % 2 != 0:
                total += digit
    return total