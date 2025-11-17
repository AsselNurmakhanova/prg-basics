def f(n):
    a = 0
    b = 1
    if n == 1:
        return a
    elif n == 2:
        return b
    for i in range(3, n+1):
        c = a + b
        a = b
        b = c
    return b
    