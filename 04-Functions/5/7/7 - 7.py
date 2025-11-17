def f(binary_number):
    for char in binary_number:
        if char not in '01':
            return False
    return True