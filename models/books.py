from models.book import Book

book1 = Book("Dune", "Frank Herbert", "Science Fiction")
book2 = Book("Necronomicon", "H.P. Lovecraft", "Cosmic Horror")
book3 = Book("Tinker, Tailor, Soldier, Spy", "John Le Carre", "Thriller")

books = [book1, book2, book3]

def add_new_book(new_book):
    books.append(new_book)

def delete_book(index):
    books.pop(int(index))