from flask import jsonify
from models.reading_model import ReadingModel
from api import db

def show_all():

    records = db.session.query(ReadingModel).all()
    readings = []
    
    for record in records:
        readings.append(record.serialize)

    return jsonify(readings)

def show(reading_id):

    record = db.session.query(ReadingModel).filter(ReadingModel.id == reading_id).first()
    reading = record.serialize

    return jsonify(reading)