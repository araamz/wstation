# Used https://python.plainenglish.io/flask-crud-application-using-mvc-architecture-3b073271274f as a basis.

from concurrent.futures import thread
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import threading

api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(api)

from routes.reading_blueprint import reading_blueprint
from routes.device_blueprint import device_blueprint

api.register_blueprint(reading_blueprint, url_prefix='/readings')
api.register_blueprint(device_blueprint, url_prefix='/device')


from devices.dht11_device import dht11_device
print("creating first singleton")
device1 = dht11_device()
print(device1.testing_val)
device1.testing_val = 5
print("creating second singleton")
device2 = dht11_device()
print(device2.testing_val)
print(device1 is device2)

from services.recorder_service import RecorderService
print(__name__)

service_class = RecorderService()
service_thread = threading.Thread(target=service_class.start_service)
service_thread.start()