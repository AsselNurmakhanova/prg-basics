def transpose_matrix(m):
    rows = len(m)
    cols = len(m[0])
    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(m[r][c])
        transposed.append(new_row)
    return transposed
