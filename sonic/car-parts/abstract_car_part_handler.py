import abc

class AbstractCarPartHandler(abc):
    '''
    Methods that logical parts of the car should have
    '''
    def __init__(self, *args, **kwargs):
        pass
    @abc.abstractmethod
    def run(self,*args, **kwargs):
        pass
    @abc.abstractmethod
    def start(self,*args, **kwargs):
        pass
    @abc.abstractmethod
    def update(self,*args, **kwargs):
        pass
    @abc.abstractmethod
    def run_threaded(self,*args, **kwargs):
        pass