import threading
class Service(threading.Thread, object):

    instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kargs):
        if not cls.instance:
            with cls.lock:
                if not cls.instance:
                    cls.instance = super(Service, cls).__new__(cls)
        return cls.instance

    def run(self):
        pass