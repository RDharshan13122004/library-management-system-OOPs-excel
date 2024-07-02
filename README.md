# Library Management System

## Overview

This Library Management System is a Python-based application that allows users to manage a collection of books, user registrations, and transactions. The system uses the `openpyxl` library to handle Excel files for storing data, and `prettytable` to display data in a tabular format.

## Features

1. **User Management**:
   - Register new users with their details.
   - View all registered users.
   - Retrieve specific user information based on name and phone number.

2. **Book Management**:
   - Add new books to the collection.
   - View all available books.
   - Retrieve specific book information based on title, author, ISBN, publisher, and category.

3. **Transaction Management**:
   - Borrow a book by creating a transaction.
   - View all transactions.
   - Return a book and update its availability.

## Dependencies

The following Python libraries are required to run the application:

- `openpyxl`: For handling Excel files.
- `prettytable`: For displaying data in a tabular format.
- `re`: For regular expression operations.

Install the dependencies using the following command:

```bash
pip install openpyxl prettytable
```

## Files

- **ib.xlsx**: Excel file used to store user, book, and transaction data.

## Classes

### `user_info`

This class handles the creation of new users and validation of their information.

#### Methods

- `__init__(self, name, age, dob, phno, email, addr)`: Initializes a new user with the provided details and validates the inputs.
- `__str__(self)`: Returns a string representation of the user information.

### `book`

This class handles the creation of new books and validation of their information.

#### Methods

- `__init__(self, title, author, isbn, publisher, year, category, available_copies)`: Initializes a new book with the provided details and validates the inputs.
- `__str__(self)`: Returns a string representation of the book information.

### `transaction`

This class handles the creation of new transactions for borrowing books.

#### Methods

- `__init__(self, user_id, book_id, borrow_date, due_date, return_date=None, status="borrowed")`: Initializes a new transaction with the provided details and validates the inputs.

### `Library`

This class provides methods to manage users, books, and transactions.

#### Methods

- `__init__(self, filename="ib.xlsx")`: Initializes the library and loads the Excel file.
- `setup_sheets(self)`: Sets up the Excel sheets if they do not exist.
- `save_wb(self)`: Saves the workbook to the file.
- `user_reg(self)`: Registers a new user.
- `view_user(self)`: Displays all registered users.
- `get_user(self)`: Retrieves user information based on name and phone number.
- `books(self)`: Adds a new book to the collection.
- `view_books(self)`: Displays all available books.
- `get_book_title(self)`: Retrieves book information based on title.
- `get_book_author(self)`: Retrieves book information based on author.
- `get_book_isbn(self)`: Retrieves book information based on ISBN.
- `get_book_publisher(self)`: Retrieves book information based on publisher.
- `get_book_category(self)`: Retrieves book information based on category.
- `transactions(self)`: Creates a new transaction for borrowing a book.
- `book_ava_cop_der(self, b_id)`: Decreases the available copies of a book.
- `view_transaction(self)`: Displays all transactions.
- `return_book(self)`: Marks a book as returned and updates its availability.

## Usage

1. **Initialize the Library**:
   ```python
   library = Library()
   ```

2. **Register a New User**:
   ```python
   library.user_reg()
   ```

3. **View All Users**:
   ```python
   library.view_user()
   ```

4. **Get User Information**:
   ```python
   library.get_user()
   ```

5. **Add a New Book**:
   ```python
   library.books()
   ```

6. **View All Books**:
   ```python
   library.view_books()
   ```

7. **Get Book Information**:
   ```python
   library.get_book_title()
   library.get_book_author()
   library.get_book_isbn()
   library.get_book_publisher()
   library.get_book_category()
   ```

8. **Create a New Transaction**:
   ```python
   library.transactions()
   ```

9. **View All Transactions**:
   ```python
   library.view_transaction()
   ```

10. **Return a Book**:
    ```python
    library.return_book()
    ```

## Notes

- Ensure that the `ib.xlsx` file is present in the same directory as the script or will be created by the script if not found.
- The system uses regular expressions to validate input data for dates, phone numbers, and email addresses.
- The transaction system checks for the availability of books and user IDs before creating a transaction.