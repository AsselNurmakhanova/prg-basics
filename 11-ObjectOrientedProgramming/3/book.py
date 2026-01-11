from bookcode import Book
def main():
    my_book = Book("George Orwell", "1984", 328)
    print(f"Author: {my_book.author}")
    print(f"Title: {my_book.title}")
    print(f"Number of Pages: {my_book.number_of_pages}")
    my_book.open_book()
    my_book.read_page(45)
    
if __name__ == "__main__":
    main()