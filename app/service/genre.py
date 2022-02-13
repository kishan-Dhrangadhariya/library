from app.models.genre import Genre
from app.utils.helper_utils import response_dict


def fetch_all_genre():
    try:
        response = Genre().fetch_all()
        return response_dict(data=response)
    except Exception as e:
        return response_dict(message=str(e), status=500)


def add_genre(kwargs):
    try:
        Genre(kwargs.get('genre_name')).create()
        return response_dict(message="data ingested successfully!!")
    except Exception as e:
        return response_dict(message=str(e), status=500)
