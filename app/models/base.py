from abc import abstractmethod
from datetime import datetime

from app import db


class Base(db.Model):
    """
    Base class def for other children classes.
    """

    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.deleted_at = None

    def create(self):
        """
        Saves the object data to DB and populates ids and dates.
        """
        db.session.add(self)
        db.session.commit()
        db.session.flush()
        return self.id

    @abstractmethod
    def to_dict(self):
        pass

    def update(self, filter_params, update_params):
        update_params["updated_at"] = datetime.now()
        db.session.query(self.__class__).filter_by(**filter_params).update(update_params)
        db.session.flush()
        db.session.commit()

    def delete(self, filter_params):
        update_params = {
            "deleted_at": datetime.now()
        }
        db.session.query(self.__class__).filter_by(**filter_params).update(update_params)
        db.session.flush()
        db.session.commit()

    def fetch_by_id(self, id):
        object_ = db.session.query(self.__class__).filter_by({"id": id}).first()
        if object:
            return object_.to_dict()
        else:
            return {}

    def fetch_by_params(self, filter_params):
        response_list = db.session.query(self.__class__).filter_by(**filter_params).all()
        dict_response = []
        for object in response_list:
            dict_response.append(object.to_dict())
        return dict_response

    def fetch_all(self):
        response_list = db.session.query(self.__class__).all()
        dict_response = []
        for object_ in response_list:
            dict_response.append(object_.to_dict())
        return dict_response
