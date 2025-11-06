
def sum_digits(number):
    v = str(abs(any_number))
    sum = 0
    for digit in v:
        sum += int(digit)
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')