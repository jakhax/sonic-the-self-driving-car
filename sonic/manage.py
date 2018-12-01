from car_parts.clock import Timestamp
from car_parts.donkey_tub_library import TubGroup, TubWriter
from car_parts.transform import Lambda,PIDController
from car_parts.camera_handler.picamera_handler import CarPiCamera
from car_parts.web_handler.donkeycar_web_handler import LocalWebController
from vehicle_handler import VehicleHandler
import os
from config import *


def drive():
    v=VehicleHandler()
    clock=Timestamp()
    cam=CarPiCamera(res=CAMERA_RESOLUTION)
    ctr=LocalWebController(use_chaos=False)

    v.add(ctr,
            inputs=["cam/image_array"],
            outputs=["user/angle","user/throttle","user/mode","recording"],
            threaded=True)
    v.add(cam, outputs=['cam/image_array'], threaded=True)
    inputs = ['cam/image_array', 'user/angle', 'user/throttle', 'user/mode', 'timestamp']
    types = ['image_array', 'float', 'float',  'str', 'str']
    tub= TubWriter(path=TUB_PATH,inputs=inputs,types=types)
    v.add(tub,inputs=inputs,run_condition="recording")
    v.start(
            rate_hz=DRIVE_LOOP_HZ,
            max_loop_count=MAX_LOOPS
            )
drive()

