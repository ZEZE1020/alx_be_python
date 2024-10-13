class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

# Creating an instance of Book
book = Book("1984", "George Orwell", 328)

# Printing the string representation
print(str(book))  # Output: 1984 by George Orwell, 328 pages

# Printing the official representation
print(repr(book)) # Output: Book('1984', 'George Orwell', 328)
