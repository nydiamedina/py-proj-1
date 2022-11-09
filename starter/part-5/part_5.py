### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def create_new_book(book_file):
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

  with open(book_file, 'a') as f:
    f.write(f'{title}, {author}, {year}, {rating}, {pages}\n')

### Step 2 - Read data from a .txt

## Now take your previously created function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def read_book_library(book_file):
  book_library = []

  with open(book_file, 'r') as f:
    file = f.readlines()

    for line in file:
      title, author, year, rating, pages = line.split(', ')
      book_library.append({
        'title': title.strip(),
        'author': author.strip(),
        'year': int(year.strip()),
        'rating': float(rating.strip()),
        'pages': int(pages.strip())
      })

  return book_library

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!
def get_book_library(books):
  print('\nHere are all your books in your library:\n')

  for book in books:
    book_information = ', '.join(f'{key.capitalize()}: {value}' for key, value in book.items())
    print(f'{book_information}\n')

def search_book_by_title(books):
  title = input('\nWhat is the title of the book you would like to search? - ')
  found_books = [book for book in books if book['title'] == title.strip()]
  print(found_books)

def remove_book_by_title(books, book_file):
  title = input('\nWhat is the title of the book you would like to remove? - ')
  books[:] = [book for book in books if book['title'] != title]

  with open(book_file, 'w') as f:
    for book in books:
      book_information = ', '.join(f'{value}' for value in book.values())
      f.write(f'{book_information}\n')
  print(f'\n{title} has been removed from your library.')

def get_total_page_count(books):
  page_count = sum([book['pages'] for book in books])
  print(f'\nThe page count of your library\'s books sums {page_count}.')

def main_menu(book_library):
  isActive = True
  while isActive:
    selection = input("""
Select 1 to add a book to your library.
Select 2 to get all your books.
Select 3 to search a book by its title.
Select 4 to remove a book by its title.
Select 5 to get the page count of all your books.
Select 6 to leave.
Selection: """)

    if selection == '1':
      create_new_book(book_library)
    elif selection == '2':
      get_book_library(read_book_library(book_library))
    elif selection == '3':
      search_book_by_title(read_book_library(book_library))
    elif selection == '4':
      remove_book_by_title(read_book_library(book_library), book_library)
    elif selection == '5':
      get_total_page_count(read_book_library(book_library))
    elif selection == '6':
      print('\nHave a nice one!')
      isActive = False
    else:
      print('\nPlease type a number corresponding to one of the options above.\n')

if __name__ == '__main__':
  main_menu('book_library.txt')