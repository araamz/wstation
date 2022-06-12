import threading
class Service(threading.Thread, object):

    _instane = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kargs):
        if not cls._instane:
            with cls._lock:
                if not cls._instane:
                    cls._instane = super(Service, cls).__new__(cls)
        return cls._instane

    def run(self):
        pass