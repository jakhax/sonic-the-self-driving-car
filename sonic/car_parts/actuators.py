import time
from car_parts.abstract_car_part_handler import AbstractCarPartHandler


import RPi.GPIO as GPIO

def map_range(x, x_mn, x_mx, y_mn, y_mx):
    # Linear mapping between two ranges of values
    x_r = x_mx - x_mn
    y_r = y_mx - y_mn
    xy_ratio = x_r / y_r
    y = ((x - x_mn) / xy_ratio + y_mn) / 1
    return float(y)

class PWM_MG996R_Steering:
    """
    Wrapper over a PWM MG996R stepper motor to convert angles to PWM pulses.
    """
    LEFT_ANGLE = -1
    RIGHT_ANGLE = 1
    def __init__(self,pin=3,freq=50,MIN_DT=2.5,MAX_DT=12.5):
        self.MIN_DT=MIN_DT
        self.MAX_DT=MAX_DT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pin=GPIO.PWM(pin, freq)
        self.pin.start(float((MAX_DT+MIN_DT)/2))
        self.thread_angle=0
        self.on=False
        
    def set_pulse(self,a):
        map_range(a, self.LEFT_ANGLE,self.RIGHT_ANGLE, self.MIN_DT, self.MAX_DT)
        if not a or not self.LEFT_ANGLE<=a<=self.RIGHT_ANGLE:
            x=map_range(0,self.LEFT_ANGLE,self.RIGHT_ANGLE,self.MIN_DT,self.MAX_DT)
            self.pin.ChangeDutyCycle(x)
        elif a == 0 or a<0 or a>0:
            x=map_range(a,self.LEFT_ANGLE,self.RIGHT_ANGLE,self.MIN_DT,self.MAX_DT)
            self.pin.ChangeDutyCycle(x)
        # elif a<0:
        #     self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2-((self.MAX_DT-self.MIN_DT)/2*-a)))
        # elif a>0:
        #     self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2+((self.MAX_DT-self.MIN_DT)/2*a)))
    def run(self,a):
        self.set_pulse(a)
    def start(self,*args, **kwargs):
        return
    def update(self,*args, **kwargs):
        self.on=True
        while self.on:
            self.set_pulse(self.thread_angle)
    def run_threaded(self,a,*args, **kwargs):
        self.thread_angle=a
        return
    def shutdown(self,*args, **kwargs):
        self.on=False
        self.pin.stop()
        GPIO.cleanup()
        return 


class PWM_L298N_Throttle:
    F_THROTTLE = 1
    B_THROTTLE = -1

    def __init__(self,pwm_pin=25,f_pin=23,b_pin=24,freq=2000,MIN_DT=0,MAX_DT=100):
        self.pwm_pin=pwm_pin
        self.f_pin=f_pin
        self.b_pin=b_pin
        self.MIN_DT=MIN_DT
        self.MAX_DT=MAX_DT
        self.MIN_DT=MIN_DT
        self.MAX_DT=MAX_DT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(f_pin,GPIO.OUT)
        GPIO.setup(b_pin,GPIO.OUT)
        GPIO.setup(pwm_pin,GPIO.OUT)
        GPIO.output(f_pin,GPIO.LOW)
        GPIO.output(b_pin,GPIO.LOW)
        self.pin=GPIO.PWM(pwm_pin,freq)
        self.pin.start(0)
        self.thread_throttle=0
        self.on=False

    def set_pulse(self,t):
        if not t or not self.B_THROTTLE<=t<=self.F_THROTTLE or t==0:
            self.pin.ChangeDutyCycle(0)
        elif t<0:
            GPIO.output(self.f_pin,GPIO.LOW)
            GPIO.output(self.b_pin,GPIO.HIGH)
            x=map_range(-t,0,1,self.MIN_DT,self.MAX_DT)
            self.pin.ChangeDutyCycle(x)
        elif t>0:
            GPIO.output(self.f_pin,GPIO.HIGH)
            GPIO.output(self.b_pin,GPIO.LOW)
            x=map_range(t,0,1,self.MIN_DT,self.MAX_DT)
            self.pin.ChangeDutyCycle(x)
    def run(self,t):
        self.set_pulse(t)
    def start(self,*args, **kwargs):
        return
    def update(self,*args, **kwargs):
        self.on=True
        while self.on:
            self.set_pulse(self.thread_throttle)
        return
    def run_threaded(self,t,*args, **kwargs):
        self.thread_throttle=t
        return
    def shutdown(self,*args, **kwargs):
        self.on=False
        self.pin.stop()
        GPIO.cleanup()
        return 
        
