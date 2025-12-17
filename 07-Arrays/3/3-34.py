def identity_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

def print_2d_array(arr):
    """
    Выводит двумерный массив в виде строк и столбцов
    """
    for row in arr:
        print(*row) 
    print()  

sizes = [3, 5, 8]

for size in sizes:
    print(f"Identity matrix {size}x{size}:")
    mat = identity_matrix(size)
    print_2d_array(mat)
