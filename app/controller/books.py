from flask_restx import Namespace, Resource, fields
from app.service.book import (
    fetch_all_books,
    fetch_book_by_string,
    add_book,
    fetch_book_by_id
)
from app.utils.helper_utils import parameter_extractor

book_namespace = Namespace("book")

add_book_model = book_namespace.model(
    "AddBook", {
        "book_name": fields.String(required=True),
        "author_name": fields.String(required=True),
        "book_description": fields.String(required=True)
    }
)

fetch_book_model = book_namespace.model(
    "BookFetchStringMatch", {
        "string": fields.String(required=True)
    }
)

fetch_book_by_id_model = book_namespace.model(
    "FetchBookByID", {
        "to": fields.Integer(required=True),
        "from": fields.Integer(required=True)
    }
)


@book_namespace.route("/fetch_by_id")
class FetchBookByID(Resource):
    @book_namespace.expect(fetch_book_by_id_model, validate=False)
    @parameter_extractor(fetch_book_by_id_model)
    def post(self, **kwargs):
        return fetch_book_by_id(kwargs)


@book_namespace.route("/fetch")
class FetchAllBook(Resource):
    def get(self):
        return fetch_all_books()


@book_namespace.route("/fetch_by_string")
class BookFetchStringMatch(Resource):
    @book_namespace.expect(fetch_book_model, validate=False)
    @parameter_extractor(fetch_book_model)
    def post(self, **kwargs):
        string = kwargs.get('string')
        return fetch_book_by_string(string)


@book_namespace.route("/add")
class AddBook(Resource):
    @book_namespace.expect(add_book_model, validate=False)
    @parameter_extractor(add_book_model)
    def post(self, **kwargs):
        return add_book(kwargs)

