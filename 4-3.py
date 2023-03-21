import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
pwm = GPIO.PWM(16,100)
while(True):
    c=int(input())
    pwm.stop()
    pwm.start(c)
    time.sleep(2)