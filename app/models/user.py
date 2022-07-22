from app.models.base import Base
from app import db


class Users(Base):

    __tablename__ = "users"

    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    user_name = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, first_name, last_name, password, user_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        super(Users, self).__init__()

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_at": self.deleted_at,
        }
