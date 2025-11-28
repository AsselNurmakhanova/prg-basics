arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_val = arr[0][0]
max_val = arr[0][0]
min_pos = (0,0)
max_pos = (0,0)

for i, row in enumerate(arr):
    for j, value in enumerate(row):
        if value < min_val:
            min_val = value
            min_pos = (i, j)
        if value > max_val:
            max_val = value
            max_pos = (i, j)

print("Minimum value:", min_val, "at row", min_pos[0], "column", min_pos[1])
print("Maximum value:", max_val, "at row", max_pos[0], "column", max_pos[1])
