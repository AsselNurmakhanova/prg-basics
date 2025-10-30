number1 = int(input ("First number: "))
number2 = int(input ("Second number: "))
operator = input ("Operator: ")
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
else:
    result = number1 / number2
print(f'{number1} {operator} {number2} = {result}')