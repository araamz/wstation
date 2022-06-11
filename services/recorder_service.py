from concurrent.futures import thread
import threading
from time import sleep

from sqlalchemy import true

from services import Service

class RecorderService:

    _instane = None
    _lock = threading.Lock()
    _active_lock = threading.Lock()

    def __new__(cls, *args, **kargs):
        if not cls._instane:
            with cls._lock:
                if not cls._instane:
                    print("CREATED NEW THREAD - " + __name__)
                    cls._instane = super(RecorderService, cls).__new__(cls)
        print("DID NOT CREATE NEW THREAD - " + __name__)
        return cls._instane

    active = True

    def start_service(self):
        #super().start_service()

        while (true):
            self._active_lock.acquire()
            if (self.active == False):
                break
            self._active_lock.release()
            sleep(2)
            print("System Run - " + str(threading.get_ident()))

            

        print("Service Stopped")
        return

    def stop_service(self):

        print("Attempt Shutdown")
        if (self._active_lock.locked()):
            print("Locked Service")
            return False

        self._active_lock.acquire()
        self.active = False
        self._active_lock.release()
        return True



