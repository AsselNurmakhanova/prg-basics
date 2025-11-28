def f(number, arr):
    greater = 0
    for j in arr:
        if j > number:
            greater += 1
    return greater
    
value = 23
numbers = [24, 23, 25, 26, 23, 245, 23]
print(f"Number of elements greater than {value}:", f(value, numbers))