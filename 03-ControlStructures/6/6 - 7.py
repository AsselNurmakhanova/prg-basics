age = int(input("Write your age: "))
if age < 14:
    print("You're a child")
elif age < 20:
    print("You're a teen")
elif age < 65:
    print("You're an adult")
else:
    print("You're a senior")