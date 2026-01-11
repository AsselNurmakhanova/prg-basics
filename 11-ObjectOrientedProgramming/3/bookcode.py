class Book:
    def __init__(self, author, title, number_of_pages):
        self.author = author
        self.title = title
        self.number_of_pages = number_of_pages
        self.book_is_open = False
        self.current_page = 0
    def open_book(self):
        self.book_is_open = True
    def close_book(self):
        self.book_is_open = False
    def read_page(self, page_number):
        if self.book_is_open:
            self.current_page = page_number
            if 1 <= self.current_page <= self.number_of_pages:
                print(f"Reading page {self.current_page} of '{self.title}'")
            else:
                print("Invalid page number.")
        else:
            print("Please open the book first.")
    def next_page(self):
        if self.book_is_open:
            if self.current_page < self.number_of_pages:
                self.current_page += 1
                print(f"Reading page {self.current_page} of '{self.title}'")
            else:
                print("You are already at the end of the book.")
        else:
            print("Please open the book first.")
    def previous_page(self):
        if self.book_is_open:
            if self.current_page > 1:
                self.current_page -= 1
                print(f"Reading page {self.current_page} of '{self.title}'")
            else:
                print("You are already at the beginning of the book.")
        else:
            print("Please open the book first.")