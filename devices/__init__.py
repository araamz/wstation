import threading
import datetime
from tokenize import String

class Device(object):

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    print(str(datetime.datetime.utcnow()) + ": " + cls.__name__ + "[SERVICE] CREATED")
                    cls._instance = super(Device, cls).__new__(cls)
        return cls._instance

    def retrieve_data(self) -> list:
        pass
