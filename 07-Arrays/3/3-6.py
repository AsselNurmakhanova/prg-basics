arr = [15, 8, 31, 47, 2, 19]
i = 0
sum = 0
while i < len(arr):
    sum += arr[i]
    i += 1
mean = sum / len(arr)
print(mean)