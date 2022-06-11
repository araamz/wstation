
from flask import jsonify
from devices.dht11_device import dht11_device
from api import service_thread

def send_live_data():

    # access device 
    # get data
    # transform data to be serialized
    testing_device = dht11_device()
    print("EXTERNAL DEVICE - " + str(testing_device.testing_val))

    return jsonify("testing")