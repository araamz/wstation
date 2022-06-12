from services import Service
from time import sleep

class RecorderService(Service):

    def run(self):
        while(True):
            sleep(5)
            print("Testing Thread")


