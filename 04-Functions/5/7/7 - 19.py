def f(number):
    number = str(number)
    count = {}
    total = 0
    for digit in number:
        if digit in count:
            count[digit] += 1
        else:
            count[digit] = 1
    for digit in count:
        if count[digit] > 1:
            total += int(digit) * count[digit]
    return total