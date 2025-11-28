def occurs(number, array):
    i = 0
    count = 0
    while i < len(array):
        for j in array:
            if number == j:
                count += 1
            i += 1
    if count != 0:
        return False
    else:
        return True
        