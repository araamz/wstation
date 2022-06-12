from services import Service
from devices.dht11_device import dht11Device
from models.reading_model import ReadingModel
from api import db
from time import sleep
import schedule

class RecorderService(Service):

    def record_data():

        weather_sensor = dht11Device().retrieve_data()
        temperature_value = weather_sensor[0]
        humidity_value = weather_sensor[1]

        record = ReadingModel(temperature = temperature_value, humidity = humidity_value)
        db.session.add(record)
        db.session.commit()

        return

    schedule.every().day.at("12:00").do(record_data)
    schedule.every().day.at("23:00").do(record_data)
    schedule.every().minute.at(":00").do(record_data)
    def run(self):
        while True:
            schedule.run_pending()
            sleep(1)


