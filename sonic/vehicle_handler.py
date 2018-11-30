import abc
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
        pass

    def add(self,*args, **kwargs):
        pass


    def start(self,*args, **kwargs):
        pass


    def update_parts(self,*args, **kwargs):
        pass

    def shutdown(self,*args, **kwargs):
        pass