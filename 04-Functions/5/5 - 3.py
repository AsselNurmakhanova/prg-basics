import keyboard # your own defined module

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter surname: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Surname: ', last_name)
print('Age: ', age)
if is_salary_hidden == True:
    print('Salary: ', salary)