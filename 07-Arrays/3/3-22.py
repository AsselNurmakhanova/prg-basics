import random
def rand_elem(array):
    num = random.randint(1, len(array))
    return array[num]
print(rand_elem([2,4,5,6,7,8]))