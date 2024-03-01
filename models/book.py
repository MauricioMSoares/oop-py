class Book:
    books = []

    def __init__(self, title, author, release_year):
        self._title = title
        self._author = author
        self._release_year = release_year
        self._available = True
        Book.books.append(self)

    def __str__(self):
        return f'{self._title.ljust(25)} | {self._author.ljust(25)} | {str(self._release_year).ljust(25)} | {self.available}'
    
    @property
    def available(self):
        return 'Available' if self._available else 'Unavailable'

    def lend(self):
        self._available = False
    
    def check_availability(year):
        available_books = []

        for book in Book.books:
            if book._release_year == year:
                available_books.append(book._title)

        return available_books
    