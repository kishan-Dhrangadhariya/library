from app.models.books import Books
from app.utils.helper_utils import response_dict


def fetch_all_books():
    try:
        response = Books().fetch_all()
        return response_dict(data=response)
    except Exception as e:
        return response_dict(message=str(e), status=500)


def fetch_book_by_string(string):
    try:
        response = Books().fetch_by_string(string)
        return response_dict(data=response)
    except Exception as e:
        return response_dict(message=str(e), status=500)


def add_book(kwargs):
    try:
        Books(kwargs).create()
        return response_dict(message="data ingested successfully!!")
    except Exception as e:
        return response_dict(message=str(e), status=500)

