arr = [2, 6, 4, 9, 7]
def star(n):
    i = 0
    total = ""
    while i < n:
        total += '*'
        i += 1
    return total

for num in arr:
    print(num, ":", star(num))