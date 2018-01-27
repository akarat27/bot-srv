from flask import Blueprint, request, render_template


admin = Blueprint('admin', __name__ , template_folder='templates')


@admin.route('books/')
def display_books():
    books = {
        "Learn Python The Hard Way": {
            "author": "Shaw, Zed",
            "rating": "3.92",
            "image": "ef0ceaab-32a8-47fb-ba13-c0b362d970da.jpg"
        }
    }

    # passing data to the template
    return render_template("books.htm", books=books)
