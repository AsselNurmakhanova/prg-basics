arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
formatted_employees = list(map(lambda arr: f"{arr[0].upper()}, {arr[1]}", arr))

for arr in formatted_employees:
    print(arr)
