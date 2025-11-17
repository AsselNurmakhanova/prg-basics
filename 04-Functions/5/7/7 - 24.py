def f(expression):
    total = 0
    sign = 1
    for char in expression:
        if char.isdigit():
            total += sign * int(char)
        if char == '+':
            sign = 1
        elif char == '-':
            sign = -1
    return total