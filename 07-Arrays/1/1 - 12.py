categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
max = max(expenses)
if max == expenses[0]:
    print(categories[0])
elif max == expenses[1]:
    print(categories[1])
elif max == expenses[2]:
    print(categories[2])
elif max == expenses[3]:
    print(categories[3])