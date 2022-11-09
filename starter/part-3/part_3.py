my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def parse_book_information (book):
    book_information = ', '.join(f'{key}: {value}' for key, value in book.items())

    return book_information

print(parse_book_information(my_book))

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_book_title(book):
    return book['title']

def get_book_author(book):
    return book['author']

def get_book_year(book):
    return book['year']

def get_book_rating(book):
    return book['rating']

def get_book_pages(book):
    return book['pages']   

# # A more reusable function:
# def get_book_property(book, property):
#     return book[f'{property}']

# print(get_book_property(my_book, 'author'))

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
def add_book_property(book, property, value):
    book[f'{property}'] = value
    return book

add_book_property(my_book, 'genre', 'Fiction')

def add_book(book_list, book):
    book_list.append(book)
    return book_list

def remove_book(book_list, book_title):
    book_list[:] = [book for book in book_list if book['title'] != book_title]
    return book_list