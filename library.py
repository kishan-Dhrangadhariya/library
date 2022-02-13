import logging as log
import argparse
from flask_migrate import init, migrate, upgrade, Migrate

from app.controller.book_genre_association import book_genre_association_namespace
from app.controller.books import book_namespace
from app.controller.genre import genre_namespace
from app import app, api, db

from constant import (
    SECRET_KEY,
    DB_CONN_POOL,
    DB_URI,
    SQLALCHEMY_ENGINE_MOD
)


class Manger:

    def __init__(self):
        self.app = app
        self.api = api
        self.logger = log
        self.add_namespace()
        self.initialise()
        Migrate(app=self.app, db=db, compare_type=True)

    def initialise(self):
        self.app.config["SECRET_KEY"] = SECRET_KEY
        self.app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
        self.app.config["DB_CONNECTION_POOL"] = DB_CONN_POOL,
        self.app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app.config["SQLALCHEMY_ENGINE_OPTIONS"] = SQLALCHEMY_ENGINE_MOD
        self.app.config["COMPRESS_ALGORITHM"] = "gzip"
        db.init_app(self.app)

    def add_namespace(self):
        self.api.add_namespace(ns=book_namespace)
        self.api.add_namespace(ns=genre_namespace)
        self.api.add_namespace(ns=book_genre_association_namespace)

    def run(self):
        self.app.run(host="127.0.0.1", port=8080)

    def list_routes(self):
        links = []
        for rule in self.app.url_map.iter_rules():
            print(rule)


if __name__ == "__main__":
    manager_obj = Manger()
    arg_parser = argparse.ArgumentParser()
    sub_parser = arg_parser.add_subparsers(dest="command")
    sub_parser.required = True
    migrate_subparser = sub_parser.add_parser("migrate")
    run_subparser = sub_parser.add_parser("run")
    list_subparser = sub_parser.add_parser('list_routes')
    migrate_subparser.add_argument("--init", action="store_true")
    migrate_subparser.add_argument("--migrate", action="store_true")
    migrate_subparser.add_argument("--upgrade", action="store_true")
    args = arg_parser.parse_args()
    print(f"args: {args}")
    if args.command == "migrate":
        with manager_obj.app.app_context():
            if args.init:
                manager_obj.logger.info("init")
                init()
            elif args.migrate:
                manager_obj.logger.info("migrate")
                migrate()
            elif args.upgrade:
                manager_obj.logger.info("upgrade")
                upgrade()
            else:
                manager_obj.logger.info("invalid args for migrate")
    if args.command == "run":
        manager_obj.logger.info("run")
        manager_obj.run()
    elif args.command == "list_routes":
        manager_obj.list_routes()