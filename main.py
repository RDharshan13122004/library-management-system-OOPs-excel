from code import Library
def main():

    user = Library()

    # register a new user
    user.user_reg()

    #view all users
    user.view_user()

    #get user information
    user.get_user()

    #add a new book
    user.books()

    #veiw all  books
    user.view_books()

    #get book information
    user.get_book_title()
    user.get_book_author()
    user.get_book_isbn()
    user.get_book_publisher()
    user.get_book_category()

    #create a new transaction
    user.transactions()
    
    #view all transaction
    user.view_transaction()

    #return a book 
    user.return_book()

if __name__ == "__main__":
    main()