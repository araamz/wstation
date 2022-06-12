import threading
class Service(threading.Thread, object):

    instane = None
    lock = threading.Lock()

    def __new__(cls, *args, **kargs):
        if not cls.instane:
            with cls.lock:
                if not cls.instane:
                    cls.instane = super(Service, cls).__new__(cls)
        return cls.instane

    def run(self):
        pass