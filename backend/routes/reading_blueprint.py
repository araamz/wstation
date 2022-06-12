from flask import Blueprint
from controllers.reading_controller import show, show_all

reading_blueprint = Blueprint('reading_blueprint', __name__)

reading_blueprint.route('/', methods=['GET'])(show_all)
reading_blueprint.route('/<int:reading_id>', methods=['GET'])(show)