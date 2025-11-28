
arr = [[0 for j in range(5)] for i in range(5)]

for i in range(5):       # строки
    for j in range(5):   # столбцы
        arr[i][j] = (i+1) * (j+1)

for row in arr:
    for value in row:
        print(f"{value:2}", end=' ') 
    print() 
