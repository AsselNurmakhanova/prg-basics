#An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and prints the array 
#  the arithmetic mean of array values. Use the “for” loop statement.

arr = [15, 8, 31, 47, 2, 19]
sum = 0
for char in arr:
    sum += char
mean = sum / len(arr)
print(mean)