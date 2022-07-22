from app.models.base import Base
from app import db
from sqlalchemy import or_, func, and_


class Books(Base):

    __tablename__ = "books"

    book_name = db.Column(db.String, unique=True)
    author_name = db.Column(db.String)
    book_description = db.Column(db.String)

    def __init__(self, data={}):
        self.book_name = data.get('book_name')
        self.author_name = data.get('author_name')
        self.book_description = data.get('book_description')
        super(Books, self).__init__()

    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author_name": self.author_name,
            "book_description": self.book_description,
        }

    def fetch_by_name(self, name):
        name = name.strip()
        response = Books.query.filter(
            func.lower(Books.book_name) == func.lower(name),
        ).first()
        if response:
            return response.to_dict()
        else:
            return {}

    def fetch_by_string(self, string):
        string = string.strip()
        string = f"%{string}%"
        response_list = Books.query.filter(
            or_(
                Books.book_name.ilike(string),
                Books.book_description.ilike(string)
            )
        ).all()
        dict_response = []
        for object_ in response_list:
            dict_response.append(object_.to_dict())
        return dict_response

    def book_between_id(self, kwargs):
        to_ = kwargs.get('to')
        from_ = kwargs.get('from')
        response_list = Books.query.filter(
            and_(
                Books.id >= from_,
                Books.id <= to_,
            )
        ).all()
        dict_response = []
        for object_ in response_list:
            dict_response.append(object_.to_dict())
        return dict_response

