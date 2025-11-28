
from MyArrays import second_largest, difference, median, min_max, as_string

numbers = [7, 3, 8, 5, 2]

print("Numbers:", ",".join(str(x) for x in numbers))
print("Second largest number:", second_largest(numbers))
print("Median:", median(numbers))
print("Smallest and largest number:", ",".join(str(x) for x in min_max(numbers)))
print("Numbers as a string:", as_string(numbers))
