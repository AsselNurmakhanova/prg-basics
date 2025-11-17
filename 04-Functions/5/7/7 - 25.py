def f(x,y):
    total = 0
    for digit in range(x, y + 1):
        if digit % 2 == 0 and digit % 3 == 0 and digit % 4 != 0:
            total += digit
    return total