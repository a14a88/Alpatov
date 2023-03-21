import RPi.GPIO as GPIO
import time

def dec2bin(value):
    binary = list(bin(value)[2::])
    if (len(binary) < 8):
            binary = binary[::-1]
            while (len(binary) < 8):
                binary.append(0)
            binary = binary[::-1]
    for i in range(len(binary)):
        binary[i] = int(binary[i])
    return binary

GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
GPIO.setup(dac, GPIO.OUT)
try:
    while (True):
        period=int(input())
        for i in range (255):
            print(int(255*(i/256)))
            GPIO.output(dac,dec2bin(int(255*(1-(i/256)))))
            time.sleep(period/512)
        for i in range (255):
            print(int(255*(1-(i/256))))
            GPIO.output(dac,dec2bin(int(255*(1-(i/256)))))
            time.sleep(period/512)
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()