from sqlalchemy import func

from app.models.base import Base
from app import db


class Genre(Base):

    __tablename__ = "genres"

    genre_name = db.Column(db.String, unique=True)

    def __init__(self, genre_name=None):
        self.genre_name = genre_name
        super(Genre, self).__init__()

    def to_dict(self):
        return {
            "id": self.id,
            "genre_name": self.genre_name,
        }

    def fetch_by_name(self, name):
        name = name.strip()
        response = Genre.query.filter(
            func.lower(Genre.genre_name) == func.lower(name),
        ).first()
        if response:
            return response.to_dict()
        else:
            return {}
