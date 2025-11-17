def f(sentence):
    new = ''
    for char in sentence:
        if char != ' ':
            new += char
    return new