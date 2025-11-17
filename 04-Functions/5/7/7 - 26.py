def f(text):
    result = ''
    for i, char in enumerate(text):
        result += char
        if i != len(text) - 1:
            result += '-'
    return result