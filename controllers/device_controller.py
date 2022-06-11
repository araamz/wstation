
from flask import jsonify
from devices.dht11_device import dht11_device
from services.recorder_service import RecorderService

def send_live_data():


    # access device 
    # get data
    # transform data to be serialized
    
    testing_device = dht11_device()
    print("EXTERNAL DEVICE - " + str(testing_device.testing_val))
    service  = RecorderService()
    service.stop_service()

    return jsonify("testing")