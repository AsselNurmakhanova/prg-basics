
import re
username = (input("Write username: "))
password = (input("Write password: "))
username_pattern = r'^[a-z]{6,}$'
password_pattern = r'^[A-Za-z0-9_]{8,}$'
username_match = re.match(username_pattern,username)
password_match = re.match(password,password_pattern)

# print results
if username_match and password_match:
   print(True)
else:
   print(False) 