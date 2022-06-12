import threading
import datetime
class Service(threading.Thread, object):

    _instane = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kargs):
        if not cls._instane:
            with cls._lock:
                if not cls._instane:
                    print(str(datetime.datetime.utcnow()) + ": " + cls.__name__ + "[SERVICE] CREATED")
                    cls._instane = super(Service, cls).__new__(cls)
        return cls._instane

    def run(self):
        pass