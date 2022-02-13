import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

db = SQLAlchemy()
app = Flask(__name__)
api = Api(app)

