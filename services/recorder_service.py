from concurrent.futures import thread
import threading
from time import sleep

from sqlalchemy import true

from services import Service

class RecorderService(Service):

    def run(self):
        while(True):
            sleep(5)
            print("Testing Thread")


