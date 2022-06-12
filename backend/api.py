# Used https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f as a basis.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(api)

from routes.reading_blueprint import reading_blueprint
from routes.device_blueprint import device_blueprint
api.register_blueprint(reading_blueprint, url_prefix='/readings')
api.register_blueprint(device_blueprint, url_prefix='/device')

from services.recorder_service import RecorderService
services = [RecorderService()]
services[0].start()

api.run(host="0.0.0.0")