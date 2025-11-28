# создаём двумерный массив 3x5
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

# вывод массива до изменений
print("Before swapping:")
for row in arr:
    print(row)

# меняем первую и последнюю строку
arr[0], arr[-1] = arr[-1], arr[0]

# вывод массива после изменений
print("\nAfter swapping:")
for row in arr:
    print(row)
