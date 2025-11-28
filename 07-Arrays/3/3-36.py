def flatten_2d(arr2d):
    flat = []
    for row in arr2d:
        for value in row:
            flat.append(value)
    return flat
