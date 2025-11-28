def f(arr1, arr2):
    for i in arr1:
        if i not in arr2:
            return False 
    return True 