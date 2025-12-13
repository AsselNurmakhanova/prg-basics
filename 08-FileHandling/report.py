###
# Calculates the total value of money spent
#
import re 
# file name with shopping report
email_file = 'report.txt'
# read the content of email
with open(email_file, 'r') as file:
    email = file.read()

# for amounts
pattern = r'\d+'
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
    total += int(amount)

print(total)