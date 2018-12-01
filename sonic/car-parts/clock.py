import datetime
from sonic.car_parts.abstract_car_part_handler import AbstractCarPartHandler

class Timestamp():

    def start(self,*args, **kwargs):
        pass

    def update(self,*args, **kwargs):
        pass

    def run_threaded(self,*args, **kwargs):
        pass

    def run(self,*args, **kwargs):
        return str(datetime.datetime.utcnow())
