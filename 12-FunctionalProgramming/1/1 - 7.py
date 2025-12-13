number = int(input("Enter a number: "))
is_even = lambda number: number % 2 == 0
if is_even(number):
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")