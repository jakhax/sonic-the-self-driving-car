import abc
import sys
from threading import Thread
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

    def add(self,part,inputs=[],outputs=[],threaded=False,run_condition=False,*args, **kwargs):
        """
        Method to add a part to the vehicle drive loop.

        Parameters
        ----------
            inputs : list
                Channel names to get from memory.
            outputs : list
                Channel names to save to memory.
            threaded : boolean
                If a part should be run in a separate thread.
            run_condition: boolean
                If a part should be run at all.
        """
        try:
            e=dict()
            e["part"]=part
            e["inputs"]=inputs
            e["outputs"]=outputs
            e["run_condition"]=run_condition
            if threaded:
                t=Thread(target=part.update,args=())
                t.daemon=True
                e["thread"]=t
            self.parts.append(e)
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