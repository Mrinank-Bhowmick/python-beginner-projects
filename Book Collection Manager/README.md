# Book Collection Manager 📚

The **Book Collection Manager** is a Python program that helps you manage a collection of books. With this program, you can perform various actions such as adding books, deleting books, searching for books by author, and saving/loading your collection to/from a file.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Functionality](#functionality)
- [Doctests](#doctests)
- [Getting Started](#getting-started)
- [License](#license)

## Features

- **Add a Book**: You can add new books to your collection by providing the book's title, author's name, and page count.

- **Delete a Book**: You have the option to delete a book from your collection by specifying its title.

- **Display All Books**: You can view a list of all the books in your collection, including their titles, authors, and page counts.

- **Search by Author**: You can search for books by a specific author, and the program will display all books by that author.

- **Save Data**: You can save your entire collection to a JSON file, allowing you to easily store and retrieve your book data.

- **Load Data**: You can load your collection from a previously saved JSON file, ensuring that your book data is persistent between program runs.

## Functionality

The code provides the following functions:

- `add_book(title, auth_name, pagecount)`: Adds a book to the collection.

- `delete_book(book_name)`: Deletes a book from the collection.

- `display_books()`: Displays all books in the collection.

- `search_by_author(author_name)`: Searches for books by a specific author.

- `save_data(filename)`: Saves the current collection to a JSON file.

- `load_data(filename)`: Loads data from a JSON file into the collection.

## Doctests

The code includes doctests for the functions, ensuring that they work correctly. You can run the doctests to verify the functionality of each function.

## Getting Started

To use the **Book Collection Manager**:

1. Clone this repository or download the code to your local machine.

2. Ensure you have Python installed on your computer (Python 3.6 or higher is recommended).

3. Open a terminal or command prompt and navigate to the directory where the code is located.

4. Run the program using the following command:
   
   ```shell
   python book_collection_manager.py

5. Follow the on-screen menu to interact with the program and manage your book collection.

You can save and load your collection by specifying a filename, allowing you to maintain your collection between program runs.
