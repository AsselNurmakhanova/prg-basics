arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[3])
print('Sum of first and last', arr[0] + arr[4])
print('Middle value', (sum(arr)/5))
for i in range(len(arr)):
    if i != len(arr) - 1:
        print(arr[i], end=" ")
    else:
        print(arr[i]) 