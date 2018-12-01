import abc
import time
from threading import Thread
from donkeycar_memory_handler import Memory
from log_handler import LogHandler

logger = LogHandler().get_logger(__name__)

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

    def __init__(self,memory=None, *args, **kwargs):
        try:
            self.mem=Memory() if not memory else memory
            self.on=True
            self.parts=[]
        except Exception as e:
            logger.exception(e)

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
                print("threaded")
            else:
                e["thread"]=None
            self.parts.append(e)
        except Exception as e:
            logger.exception(e)

    def start(self,rate_hz=10,test_loop_count=0,*args, **kwargs):
        try:
            self.on=True
            # run threaded parts
            for en in self.parts:
                if en["thread"]:en.get("thread").start()
            count=0          
            while self.on:
                start_time=time.time()
                self.update_parts()
                count +=1
                if test_loop_count and test_loop_count<count:
                    self.on=False
                sleep_time= (1.0/rate_hz)-(time.time()-start_time)
                if sleep_time > 0.0:
                    time.sleep(sleep_time)
                  
        except Exception as e:
            logger.exception(e)
        finally:
            self.shutdown()

    def update_parts(self,*args, **kwargs):
        try:
            for en in self.parts:
                run=True
                if en.get("run_condition"):
                    run=self.mem.get([en.get("run_condition")])[0]
                if run:
                    p=en["part"]
                    inputs=self.mem.get(en["inputs"])
                    outputs=p.run_threaded(*inputs) if en["thread"] else p.run(*inputs)
                    if outputs is not None:
                        self.mem.put(en["outputs"],outputs)
        except Exception as e:
            logger.exception(e)

    def shutdown(self,*args, **kwargs):
        try:
            logger.info("Shutting down vehicle")
            for entry in self.parts:
                entry["part"].shutdown()
        except Exception as e:
            logger.exception(e)
