def f(name):
    words = name.split()
    result = ''
    for i in words:
        result += i[0].upper()
    return result