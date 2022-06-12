from api import db

class ReadingModel(db.Model):

    __tablename__ = 'readings'

    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Integer)
    temperature = db.Column(db.Integer)
    recorded_on = db.Column(db.DateTime, server_default=db.func.now())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'humidity': self.humidity,
            'temperature': self.temperature,
            'recorded_on': self.recorded_on
        }