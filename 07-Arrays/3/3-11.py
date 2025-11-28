def bubblesort(array):
    for pass_number in range(len(array) - 1):
        for j in range(len(array) - 1 - pass_number):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubblesort([2,4,6,7,3,5]))