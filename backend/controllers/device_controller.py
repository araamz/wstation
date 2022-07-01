from flask import jsonify
from api import db
from devices.dht11_device import dht11Device

def check_alive():

    alive_message = { "alive": True }
    return jsonify(alive_message)

def show_reading():

    weather_sensor = dht11Device().retrieve_data()
    temperature_value = weather_sensor[0]
    humidity_value = weather_sensor[1]

    serialized_data = {
        'humidity': humidity_value,
        'temperature': temperature_value,
    }

    return jsonify(serialized_data)

