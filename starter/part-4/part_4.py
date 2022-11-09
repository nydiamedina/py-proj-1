### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def create_new_book():
#   title = input('What is the title of the book you would like to add? - ')
#   author = input('Who is the author of the book you would like to add? - ')
#   year = input('What year was this book published? - ')
#   rating = input('What rating out of 5 would you give this book? - ')
#   pages = input('What is the page count of the book? - ')

#   book_dictionary = {
#     'title': title,
#     'author': author,
#     'year': year,
#     'rating': rating,
#     'pages': pages
#   }

#   return book_dictionary

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_new_book():
#   title = input('What is the title of the book you would like to add? - ')
#   author = input('Who is the author of the book you would like to add? - ')
#   year = int(input('What year was this book published? - '))
#   rating = float(input('What rating out of 5 would you give this book? - '))
#   pages = int(input('What is the page count of the book? - '))

#   book_dictionary = {
#     'title': title,
#     'author': author,
#     'year': year,
#     'rating': rating,
#     'pages': pages
#   }

#   return book_dictionary

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
# def create_new_book():
#   title = input('What is the title of the book you would like to add? - ')
#   author = input('Who is the author of the book you would like to add? - ')
#   try:
#     year = int(input('What year was this book published? - '))
#   except:
#     year = int(input('Please type a number for the year? - '))
#   try:
#     rating = float(input('What rating out of 5 would you give this book? - '))
#   except:
#     rating = float(input('Please type a number between 0 and 5 for the rating? - '))
#   try:
#     pages = int(input('What is the page count of the book? - '))
#   except:
#     pages = int(input('Please type a number for the page count? - '))

#   book_dictionary = {
#     'title': title,
#     'author': author,
#     'year': year,
#     'rating': rating,
#     'pages': pages
#   }

#   return book_dictionary

# print(create_new_book())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
# def main_menu():
#   selection = input('Select 1 to add a book to your library.\nSelect 2 to get all your books.\nSelect 3 to search a book by its title.\nSelection: ')

#   if selection == '1':
#     # Call create a book function
#     pass
#   elif selection == '2':
#     # Call get all books function
#     pass
#   elif selection == '3':
#     # Call search book by title function
#     pass
#   else:
#     print('\nPlease type a number corresponding to one of the options above.\n')

# main_menu()

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
book_library = [
  {
    "title": "Atomic Habits",
    "author": "James Clear",
    "year": 2018,
    "rating": 4.38,
    "pages": 319
  },
  {
    "title": "Deep Work",
    "author": "Cal Newport",
    "year": 2016,
    "rating": 4.19,
    "pages": 296
  },
  {
    "title": "Big Magic",
    "author": "Elizabeth Gilbert",
    "year": 2015,
    "rating": 3.95,
    "pages": 276
  },
  {
    "title": "Digital Minimalism",
    "author": "Cal Newport",
    "year": 2019,
    "rating": 4.07,
    "pages": 302
  },
  {
    "title": "Anna and the French Kiss",
    "author": "Stephanie Perkins",
    "year": 2010,
    "rating": 3.99,
    "pages": 328
  }
]

def create_new_book():
  title = input('What is the title of the book you would like to add? - ')
  author = input('Who is the author of the book you would like to add? - ')
  try:
    year = int(input('What year was this book published? - '))
  except:
    year = int(input('Please type a number for the year? - '))
  try:
    rating = float(input('What rating out of 5 would you give this book? - '))
  except:
    rating = float(input('Please type a number between 0 and 5 for the rating? - '))
  try:
    pages = int(input('What is the page count of the book? - '))
  except:
    pages = int(input('Please type a number for the page count? - '))

  book_dictionary = {
    'title': title,
    'author': author,
    'year': year,
    'rating': rating,
    'pages': pages
  }
  print(book_dictionary)

  return book_dictionary

def get_all_books(books):
  print('\nHere are all your books in your library:\n')

  for book in books:
    book_information = ', '.join(f'{key.capitalize()}: {value}' for key, value in book.items())
    print(f'{book_information}\n')

def search_book_by_title(books):
  title = input('What is the title of the book you would like to search? - ')
  print([book for book in books if book['title'] == title.strip()])

def main_menu(books):
  isActive = True
  while isActive:
    selection = input('Select 1 to add a book to your library.\nSelect 2 to get all your books.\nSelect 3 to search a book by its title.\nSelect 4 to leave.\nSelection: ')

    if selection == '1':
      books.append(create_new_book()) 
    elif selection == '2':
      get_all_books(books)
    elif selection == '3':
      search_book_by_title(books)
    elif selection == '4':
      print('\nHave a nice one!')
      isActive = False
    else:
      print('\nPlease type a number corresponding to one of the options above.\n')

main_menu(book_library)