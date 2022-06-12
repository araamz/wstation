from flask import Blueprint
from controllers.device_controller import show_live_data

device_blueprint = Blueprint('device_blueprint', __name__)

device_blueprint.route('/live_data', methods=['GET'])(show_live_data)