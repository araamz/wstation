from time import sleep

from services import Service

class RecorderService(Service):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            print(__name__ + " SEEN AND ACCESSED")
            cls.instance = super(RecorderService, cls).__new__(cls)
        return cls.instance

    active = False

    def start_service(self):
        super().start_service()

        self.active = True

        while (self.active):

            sleep(2)
            print("System Run")

        return

    def stop_service(self):

        self.active = False