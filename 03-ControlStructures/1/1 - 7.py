basic_salary = 5000
total_salary = 0
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'
if is_bonus:
    bonus = int(input("Write bonus %: ")) #because in task % of bonus is different (15% and 30%)
    total_salary = basic_salary + (basic_salary * (bonus * 0.01))
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')