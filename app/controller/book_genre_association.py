from flask_restx import Namespace, Resource, fields
from app.service.book_genre_association import add_genre_to_book, fetch_book_by_genre
from app.utils.helper_utils import parameter_extractor

book_genre_association_namespace = Namespace("book_genre_association")

add_book_genre_association_model = book_genre_association_namespace.model(
    "AddBookToGenre", {
        "genre_name": fields.String(required=True),
        "books": fields.List(fields.Integer(), required=True)
    }
)

fetch_book_genre_association_model = book_genre_association_namespace.model(
    "FetchBookToGenre", {
        "genre_name": fields.String(required=True)
    }
)


@book_genre_association_namespace.route("/add")
class AddBookToGenre(Resource):
    @book_genre_association_namespace.expect(add_book_genre_association_model, validate=False)
    @parameter_extractor(add_book_genre_association_model)
    def post(self, **kwargs):
        return add_genre_to_book(kwargs)


@book_genre_association_namespace.route("/fetch")
class FetchBookToGenre(Resource):
    @book_genre_association_namespace.expect(fetch_book_genre_association_model, validate=False)
    @parameter_extractor(fetch_book_genre_association_model)
    def post(self, **kwargs):
        return fetch_book_by_genre(kwargs)
