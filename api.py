# Used https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f as a basis.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(api)

from models.reading_model import reading_model
from routes.reading_blueprint import reading_blueprint
api.register_blueprint(reading_blueprint, url_prefix='/reading')