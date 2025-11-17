def f(number1, number2, number3):
    if number1 >= number2 and number1 >= number3:
        largest = number1
    elif number2 >= number1 and number2 >= number3:
        largest = number2
    elif number3 >= number1 and number3 >= number2:
        largest = number3
    if number1 <= number2 and number1 <= number3:
        smallest = number1
    elif number2 <= number1 and number2 <= number3:
        smallest = number2
    elif number3 <= number1 and number3 <= number2:
        smallest = number3
    return largest - smallest