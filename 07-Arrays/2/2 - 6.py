arr = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
i = 0
for char in arr:
    arr[i][i] = 1
    i += 1
print(arr)