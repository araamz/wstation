from flask import jsonify
from models.reading_model import reading_model
from api import db

def show_all():

    records = db.session.query(reading_model).all()
    readings = []
    
    for record in records:
        readings.append(record.serialize)

    return jsonify(readings)

def show(reading_id):

    record = db.session.query(reading_model).filter(reading_model.id == reading_id).first()
    reading = record.serialize

    return jsonify(reading)