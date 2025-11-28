arr = [2, 3, 2, 5, 8, 1, 9, 8]

unique = []

for num in arr:
    if arr.count(num) == 1:
        unique.append(num)

print("Array:", *arr)
print("Unique elements:", *unique)
