import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from sonic.car_parts.abstract_car_part_handler import AbstractCarPartHandler


class CarPiCamera(AbstractCarPartHandler):
    def __init__(self,res=(120,160),framerate=20, *args, **kwargs):
        self.camera=PiCamera()
        self.camera.resolution=(res[1],res[0])
        self.camera.framerate=framerate
        self.raw_cap=PiRGGArray(self.camera,size=res)
        self.stream=self.camera.capture_continuous(self.raw_cap,format="rgb",use_video_port=True)
        self.frame=None
        self.on=True
        print("Camera loaded")
        time.sleep(2)

    def run(self,*args, **kwargs):
        pass
 
    def start(self,*args, **kwargs):
        pass

    def update(self,*args, **kwargs):
        pass

    def run_threaded(self,*args, **kwargs):
        pass
