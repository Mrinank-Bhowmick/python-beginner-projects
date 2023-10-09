import json

# Initialize data as an empty list to hold book information.
data = []

def add_book(title, auth_name, pagecount):
    """
    Add a new book to the collection.

    Args:
        title (str): The title of the book.
        auth_name (str): The author's name.
        pagecount (int): The number of pages in the book.

    Returns:
        None
    """
    book = {"Title": title, "Author": auth_name, "Page Count": pagecount}
    data.append(book)

def delete_book(book_name):
    """
    Delete a book from the collection.

    Args:
        book_name (str): The title of the book to be deleted.

    Returns:
        None
    """
    for book in data:
        if book["Title"] == book_name:
            data.remove(book)
            print(f"Book '{book_name}' has been deleted.")
            return
    print(f"Book '{book_name}' not found in the collection.")

def display_books():
    """
    Display all books in the collection.

    Returns:
        None
    """
    for i, book in enumerate(data):
        print(f"{i+1}. Title: {book['Title']}, Author: {book['Author']}, Page Count: {book['Page Count']}")

def search_by_author(author_name):
    """
    Search for books by a specific author.

    Args:
        author_name (str): The name of the author to search for.

    Returns:
        None
    """
    found_books = [book for book in data if author_name.lower() in book['Author'].lower()]
    if found_books:
        print(f"Books by '{author_name}':")
        for book in found_books:
            print(f"Title: {book['Title']}, Page Count: {book['Page Count']}")
    else:
        print(f"No books found by '{author_name}'.")

def save_data(filename):
    """
    Save the current data to a JSON file.

    Args:
        filename (str): The name of the file to save the data to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("Data saved successfully.")

def load_data(filename):
    """
    Load data from a JSON file.

    Args:
        filename (str): The name of the file to load data from.

    Returns:
        None
    """
    global data
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("File not found. Starting with an empty collection.")

# The following block is for running the code as a standalone script.
if __name__ == '__main__':
    filename = "book_data.json"

    # Load data from a file if it exists
    load_data(filename)

    while True:
        print("\nBook Collection Manager")
        print("1. Add a Book")
        print("2. Delete a Book")
        print("3. Display All Books")
        print("4. Search by Author")
        print("5. Save Data")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the author's name: ")
            page_count = int(input("Enter the page count: "))
            add_book(title, author, page_count)
            print(f"Book '{title}' added to the collection.")

        elif choice == '2':
            book_name = input("Enter the book title to delete: ")
            delete_book(book_name)

        elif choice == '3':
            display_books()

        elif choice == '4':
            author_name = input("Enter the author's name to search: ")
            search_by_author(author_name)

        elif choice == '5':
            save_data(filename)

        elif choice == '6':
            save_data(filename)
            break
