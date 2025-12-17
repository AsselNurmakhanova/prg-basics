import csv
filename = 'it_company.csv'
print("GRAPHIC DESIGNERS")
print("=================")
with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile) # reads each row as a dictionary using headers as keys
    for row in reader:
        if row['Job Title'] == 'Graphic Designer':
            # выводим First Name, Last Name, Email через запятую
            print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
