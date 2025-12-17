# создаём двумерный массив 3x5
arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
# меняем первый и последний column
for row in arr:
    row[0], row[-1] = row[-1], row[0]
print("\nAfter swapping columns:")
for row in arr:
    print(row)
