from flask import Blueprint
from flask_cors import CORS
from controllers.device_controller import show_reading, check_alive

device_blueprint = Blueprint('device_blueprint', __name__)
CORS(device_blueprint)

device_blueprint.route("/alive", methods=["GET"])(check_alive)
device_blueprint.route('/live/reading', methods=['GET'])(show_reading)