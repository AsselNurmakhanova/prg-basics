it = 'it_company.csv'
with open(it, 'r') as file:
    count = 0
    for line in file:
        print(line, end='')  # end='' чтобы не было двойного переноса
        count += 1
        if count % 5 == 0:  # после каждой пятой строки
            input("Press Enter key...")
            