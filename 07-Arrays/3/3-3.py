#Create a program that computes the second power of each array element. Sample result:

#array: 8 2 5 1 9
#2nd power: 64 4 25 1 81

arr = [8,2,5,1,9]
i = 0
while i < len(arr):
    new = arr[i] ** 2
    print(new, end=" ")
    i += 1