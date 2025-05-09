#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, jsonify, abort, make_response
app = Flask(__name__)

# An array that will hold books
books = [
    {
        "id": 1,
        "title": "CS50",
        "description": "Intro to CS and art of programming!",
        "author": "Harvard",
        "borrowed": False
    },
    {
        "id": 2,
        "title": "Python 101",
        "description": "little python code book.",
        "author": "Will",
        "borrowed": False
    }
]

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# get and jsonify the data
@app.route("/bookapi/books")
def get_books():
    """ function to get all books """
    return jsonify({"Books": books})


# get book by provided 'id'
@app.route("/bookapi/books/<int:book_id>", methods=['GET'])
def get_by_id(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)
    return jsonify({"Book": books[0]})


#error handling
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found!"}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({"error": "Bad request!"}), 400)


if __name__ == '__main__':
    app.run(debug=True)
