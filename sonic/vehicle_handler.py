import abc
import sys
from sonic.log_handler import LogHandler

log_handler = LogHandler()
log_handler.create_logger(__name__)

class AbstractVehicleHandler(abc.ABC):


    def __init__(self, *args, **kwargs):
        pass
    @abc.abstractmethod
    def add(self,*args, **kwargs):
        pass

    @abc.abstractmethod
    def start(self,*args, **kwargs):
        pass

    @abc.abstractmethod
    def update_parts(self,*args, **kwargs):
        pass

    @abc.abstractmethod
    def shutdown(self,*args, **kwargs):
        pass

class VehicleHandler(AbstractVehicleHandler):

    def __init__(self, *args, **kwargs):
        try:
            self.on=True
            self.parts=[]
        except Exception as e:
            log_handler.logError(sys.exc_info(), e)

    def add(self,*args, **kwargs):
        try:
            pass
        except Exception as e:
            log_handler.logError(sys.exc_info(), e)

    def start(self,*args, **kwargs):
        try:
            pass
        except Exception as e:
            log_handler.logError(sys.exc_info(), e)

    def update_parts(self,*args, **kwargs):
        try:
            pass
        except Exception as e:
            log_handler.logError(sys.exc_info(), e)

    def shutdown(self,*args, **kwargs):
        try:
            pass
        except Exception as e:
            log_handler.logError(sys.exc_info(), e)