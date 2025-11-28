def identity_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])          
        for col in range(n):
            if row == col:
                matrix[row].append(1)
            else:
                matrix[row].append(0)
    return matrix

def print_2d(arr):
    for row in arr:
        print(row)
    print() 

print(print_2d(identity_matrix(3)))