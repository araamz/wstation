from http import HTTPStatus
from flask import Response, jsonify
from api import db
from devices.dht11_device import dht11Device

def check_alive():

    return jsonify(), 200

def show_reading():

    weather_sensor = dht11Device().retrieve_data()
    temperature_value = weather_sensor[0]
    humidity_value = weather_sensor[1]

    serialized_data = {
        'humidity': humidity_value,
        'temperature': temperature_value,
    }

    return jsonify(serialized_data)

