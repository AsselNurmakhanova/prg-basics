arr = [7,9,2,4,5,6]
even = []
odd = []
j = 0
for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
new_arr = even + odd
print(new_arr)