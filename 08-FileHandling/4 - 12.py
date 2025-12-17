import csv
# ---------------------------------------
# Возвращает имя файла по жанру
def get_filename_by_genre(genre):
    mapping = {
        "Fantasy": "books_fantasy.txt",
        "Historical": "books_historical.txt",
        "Romance": "books_romance.txt",
        "Classic": "books_classic.txt"
    }
    return mapping.get(genre)
# ---------------------------------------
# Копирует книги по жанрам
def copy_books(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            genre = row["Genre"]
            filename = get_filename_by_genre(genre)
            if filename:
                with open(filename, 'a') as g:
                    g.write(
                        f"{row['Title']}, {row['Author']}, {row['Year']}\n")
# ---------------------------------------
# Основная функция
def main():
    copy_books("books.csv")
    print("Books copied successfully.")
main()
