items = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
for item, quantity in items.items():
    print(f"{item}: {quantity}")
sum = 0
for quantity in items.values():
    sum += quantity
print(f"Total items in inventory: {sum}")