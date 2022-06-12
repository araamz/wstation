
from flask import jsonify
from devices.dht11_device import dht11Device

def show_live_data():

    weather_sensor = dht11Device().retrieve_data()
    temperature_value = weather_sensor[0]
    humidity_value = weather_sensor[1]

    serialized_data = {
        'humidity': humidity_value,
        'temperature': temperature_value,
    }

    return jsonify(serialized_data)