import csv
filename = 'clothing.csv'
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile) # reads each row as a dictionary using headers as keys
    for row in reader:
        if row['Price'] < '60' and row['Stock_Quantity'] < '40':
            print(f"{row['Product_Name']},{row['Size']},{row['Price']}")