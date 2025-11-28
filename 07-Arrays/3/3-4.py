#An array contains numbers: -15, 8, -31, 47, -2, 19. Create a program that finds and prints the maximum and minimum number. 
# Do not use available functions.

arr = [-15, 8, -31, 47, -2, 19]
max_num = arr[0]
min_num = arr[0]
i = 1
while i < len(arr):
    if arr[i] > max_num:
        max_num = arr[i]
    if arr[i] < min_num:
        min_num = arr[i]
    i += 1

print("Maximum number:", max_num)
print("Minimum number:", min_num)
