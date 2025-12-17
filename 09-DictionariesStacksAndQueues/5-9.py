import csv
letters_to_province = {}
province = 'province.csv'
with open(province, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        letters_to_province[row['Letter']] = row['Name']
province_count = {province: 0 for province in letters_to_province.values()}
with open('vehicle.txt') as f:
    for line in f:
        reg_number = line.strip()  # убираем пробелы и переносы строк
        if not reg_number:
            continue
        first_letter = reg_number[0].upper()  # первая буква номера
        province = letters_to_province.get(first_letter)
        if province:
            province_count[province] += 1
for province, count in province_count.items():
    print(f"{province}: {count} vehicle(s)")
