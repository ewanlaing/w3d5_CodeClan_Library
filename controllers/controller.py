from flask import render_template, request, redirect
from app import app
from models.book import *
from models.books import books, add_new_book, delete_book

@app.route("/")
def index():
    return render_template("index.html", books=books)


@app.route("/home")
def home():
    return render_template("index.html", books=books)

@app.route("/home/<index>")
def show_book(index):
    book = books[int(index)]
    return render_template("book.html", book=book)

@app.route("/home", methods=["POST"])
def add_book():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    add_new_book(new_book)
    return render_template("index.html", books=books)

@app.route("/home/delete/<index>", methods=["POST"])
def remove_book(index):
    delete_book(index)
    return render_template("index.html", books=books)