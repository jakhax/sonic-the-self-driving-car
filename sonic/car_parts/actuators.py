import time
from car_parts.abstract_car_part_handler import AbstractCarPartHandler


class PWM_MG996R_Steering:
    """
    Wrapper over a PWM MG996R stepper motor to convert angles to PWM pulses.
    """
    LEFT_ANGLE = -1
    RIGHT_ANGLE = 1
    def __init__(self,pin=3,freq=50,MIN_DT=2.5,MAX_DT=12.5):
        import RPi.GPIO as GPIO
        self.MIN_DT=MIN_DT
        self.MAX_DT=MAX_DT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pin=GPIO.PWM(pin, freq)
        self.pin.start(float((MAX_DT+MIN_DT)/2))
        
    def set_pulse(self,a):
        print(a)
        if not a or not self.LEFT_ANGLE<=a<=self.RIGHT_ANGLE:self.pin.ChangeDutyCycle(((self.MAX_DT+self.MIN_DT)/2))
        elif a == 0:
            self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2))
        elif a<0:
            self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2-((self.MAX_DT-self.MIN_DT)/2*-a)))
        elif a>0:
            self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2-((self.MAX_DT-self.MIN_DT)/2*-a)))
        time.sleep(0.5)
    def run(self,a):
        self.set_pulse(a)
    def start(self,*args, **kwargs):
        return
    def update(self,*args, **kwargs):
        return
    def run_threaded(self,*args, **kwargs):
        return
    def shutdown(self,*args, **kwargs):
        self.pin.stop()
        GPIO.cleanup()
        return 
