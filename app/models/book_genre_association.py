from app.models.base import Base
from app import db
from sqlalchemy import func


class BookGenreAssociation(Base):

    __tablename__ = "book_genre_association"

    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    def __init__(self, data_dict={}):
        self.genre_id = data_dict.get('genre_id')
        self.book_id = data_dict.get('book_id')
        super(BookGenreAssociation, self).__init__()

    def to_dict(self):
        return {
            "id": self.id,
            "genre_id": self.genre_id,
            "book_id": self.book_id
        }

    def fetch_book_by_genre(self, string):
        from app.models.genre import Genre
        from app.models.books import Books
        string = string.strip()
        response_list = Books.query.join(BookGenreAssociation).join(Genre).filter(
            func.lower(Genre.genre_name) == func.lower(string)
        ).all()
        dict_response = []
        for object_ in response_list:
            dict_response.append(object_.to_dict())
        return dict_response

    def add_genre_to_book(self, kwargs):
        genre = kwargs.get('genre_name')
        books = kwargs.get('books')
        from app.models.genre import Genre
        genre = genre.strip()
        object_ = Genre().fetch_by_name(genre)
        if not object_:
            genre_id = Genre(genre_name=genre).create()
        else:
            genre_id = object_.get('id')
        for book_id in books:
            BookGenreAssociation(
                data_dict={
                    "genre_id": genre_id,
                    "book_id": book_id
                }
            ).create()

