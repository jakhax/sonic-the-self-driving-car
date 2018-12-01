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
        self.thread_angle=0
        
    def set_pulse(self,a):
        print(a)
        if not a or not self.LEFT_ANGLE<=a<=self.RIGHT_ANGLE:self.pin.ChangeDutyCycle(((self.MAX_DT+self.MIN_DT)/2))
        elif a == 0:
            self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2))
        elif a<0:
            self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2-((self.MAX_DT-self.MIN_DT)/2*-a)))
        elif a>0:
            self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2+((self.MAX_DT-self.MIN_DT)/2*a)))
        time.sleep(0.5)
    def run(self,a):
        self.set_pulse(a)
    def start(self,*args, **kwargs):
        return
    def update(self,*args, **kwargs):
        self.set_pulse(self.thread_angle)
        return
    def run_threaded(self,a,*args, **kwargs):
        self.thread_angle=a
        return
    def shutdown(self,*args, **kwargs):
        self.pin.stop()
        GPIO.cleanup()
        return 


class PWM_L298N_Throttle:
    F_THROTTLE = 1
    B_THROTTLE = -1

    def __init__(self,pwm_pin=25,f_pin=24,b_pin=23,freq=1000,MIN_DT=10,MAX_DT=90):
        for k,v in kwargs.items():
            setattr(self,k,v)
        import RPi.GPIO as GPIO
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

    def set_pulse(self,t):
        if not t or not self.B_THROTTLE<=a<=self.F_THROTTLE:self.pin.ChangeDutyCycle(0)
        elif t == 0:
            self.pin.ChangeDutyCycle(0)
        elif a<0:
            GPIO.output(self.f_pin,GPIO.LOW)
            GPIO.output(self.b_pin,GPIO.HIGH)
            self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2-((self.MAX_DT-self.MIN_DT)/2*-t)))
        elif a>0:
            GPIO.output(self.f_pin,GPIO.HIGH)
            GPIO.output(self.b_pin,GPIO.LOW)
            self.pin.ChangeDutyCycle(float((self.MAX_DT+self.MIN_DT)/2+((self.MAX_DT-self.MIN_DT)/2*t)))
    def run(self,t):
        self.set_pulse(t)
    def start(self,*args, **kwargs):
        return
    def update(self,*args, **kwargs):
        self.set_pulse(self.thread_throttle)
        return
    def run_threaded(self,t,*args, **kwargs):
        self.thread_throttle=a
        return
    def shutdown(self,*args, **kwargs):
        self.pin.stop()
        GPIO.cleanup()
        return 
        