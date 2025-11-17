def f(product_code):
    if len(product_code) != 4:
        return False
    sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    if sum % 7 == int(product_code[3]):
        return True
    else:
        return False