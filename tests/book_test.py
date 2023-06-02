import unittest
from models.book import Book
from models.books import *

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("Dune", "Frank Herbert", "Science Fiction")
        self.book2 = Book("Necronomicon", "H.P. Lovecraft", "Cosmic Horror")
        self.book3 = Book("Tinker, Tailor, Soldier, Spy", "John Le Carre", "Thriller")

    def test_book_has_title(self):
        self.assertEqual("Dune", self.book1.title)

    def test_book_has_author(self):
        self.assertEqual("Frank Herbert", self.book1.author)

    def test_book_has_genre(self):
        self.assertEqual("Science Fiction", self.book1.genre)

 


