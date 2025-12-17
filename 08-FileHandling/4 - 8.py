import re
with open('files.txt', 'r') as f:
        files = f.readlines()
    # Проходим по каждой строке
for file in files:
    file = file.strip()  # удаляем пробелы и перенос строки
    if re.search(r'\.[a-zA-Z0-9]{4}$', file):
        print(file)