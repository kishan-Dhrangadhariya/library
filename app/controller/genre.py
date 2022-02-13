from app.service.genre import add_genre, fetch_all_genre
from flask_restx import Namespace, Resource, fields
from app.utils.helper_utils import parameter_extractor

genre_namespace = Namespace("genre")

genre_book_model = genre_namespace.model(
    "AddGenre", {
        "genre_name": fields.String(required=True)
    }
)


@genre_namespace.route("/fetch")
class FetchAllGenre(Resource):
    def get(self):
        return fetch_all_genre()


@genre_namespace.route("/add")
class AddGenre(Resource):
    @genre_namespace.expect(genre_book_model, validate=False)
    @parameter_extractor(genre_book_model)
    def post(self, **kwargs):
        return add_genre(kwargs)