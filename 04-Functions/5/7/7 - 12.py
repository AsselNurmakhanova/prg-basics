def f(n):
    i = 0
    result = ""
    while i < n:
        result += '*'
        if i < n-1:
            result += '/'
        i +=1
    return result