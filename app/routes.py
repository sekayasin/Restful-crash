from app import app
from flask import jsonify

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 9780394800165
    },
    {
        'name': 'The Cat in the Hat',
        'price': 6.99,
        'isbn': 97802371000193
    }
]

#Welcome to the book store


#GET /store
@app.route('/books')
def get_books():
    return jsonify({'books': books})

#GET /books/9780394800165
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value = {}
    for book in books:
        if book["isbn"] == isbn:
            return_value = {
                'name': book["name"],
                'price': book["price"]
            }
    return jsonify(return_value)