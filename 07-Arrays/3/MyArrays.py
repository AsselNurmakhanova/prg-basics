# MyArrays.py

def second_largest(arr):
    largest = second = float('-inf')
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second

def difference(arr):
    smallest = largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest - smallest

def median(arr):
    # Сначала сортируем массив (bubble sort)
    n = len(arr)
    sorted_arr = arr[:]  # копия массива
    for i in range(n-1):
        for j in range(n-1-i):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    
    if n % 2 == 1:
        return sorted_arr[n // 2]
    else:
        mid1 = sorted_arr[n//2 - 1]
        mid2 = sorted_arr[n//2]
        return (mid1 + mid2) / 2

def min_max(arr):
    smallest = largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return [smallest, largest]

def as_string(arr):
    result = ""
    for i, num in enumerate(arr):
        result += str(num)
        if i != len(arr)-1:
            result += "-"
    return result
