import datetime
from sonic.car_parts.abstract_car_part_handler import AbstractCarPartHandler

class Timestamp(AbstractCarPartHandler):

    def start(self,*args, **kwargs):
        return

    def update(self,*args, **kwargs):
        return

    def run_threaded(self,*args, **kwargs):
        return

    def run(self,*args, **kwargs):
        return str(datetime.datetime.utcnow())

    def shutdown(self,*args, **kwargs):
        return
