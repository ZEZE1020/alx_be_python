# Function to get book information from the user
def get_book_info():
    # Initialize an empty dictionary to store book information
    book_info = {}
    
    # Get user input for the book's title, author, and genre
    book_info['title'] = input("Enter the title of your favorite book: ")
    book_info['author'] = input("Enter the author of your favorite book: ")
    book_info['genre'] = input("Enter the genre of your favorite book: ")
    
    return book_info

# Function to retrieve the genre of the book
def get_genre(book):
    return book.get('genre', 'Genre not found')

# Main function
def main():
    # Get the book information from the user
    favorite_book = get_book_info()
    
    # Retrieve and print the genre of the favorite book
    genre = get_genre(favorite_book)
    print(f"The genre of your favorite book  is {genre}")

# Run the main function
if __name__ == "__main__":
    main()
