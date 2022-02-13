from app.utils.helper_utils import response_dict
from app.models.book_genre_association import BookGenreAssociation


def add_genre_to_book(kwargs):
    try:
        BookGenreAssociation().add_genre_to_book(kwargs)
        return response_dict(message="data ingested successfully!!")
    except Exception as e:
        return response_dict(message=str(e), status=500)


def fetch_book_by_genre(kwargs):
    try:
        response = BookGenreAssociation().fetch_book_by_genre(kwargs.get('genre_name'))
        return response_dict(data=response)
    except Exception as e:
        return response_dict(message=str(e), status=500)
