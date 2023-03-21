import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26,19,13,6,5,11,9,10]
GPIO.setup(dac, GPIO.OUT)
try:
    value = input()
    while (value != "q"):
        if(value[0] == "-"):
            print("value should not be less then 0")
        elif (not value.isdigit()):
            print("value should be a number")
        elif (not value.isdecimal()):
            print("value should be an integer")
        else:
            value = int(value)
            if( value > 255):
                print("number too big")
            else:
                binary = list(bin(value)[2::])
                for i in range(len(binary)):
                    binary[i] = int(binary[i])
                if (len(binary) < 8):
                    binary = binary[::-1]
                    while (len(binary) < 8):
                        binary.append(0)
                    binary = binary[::-1]
                GPIO.output(dac,binary)
                voltage=str(3.3/255*value)
                if (len(voltage)>5):
                    print(voltage[0:4:])
                else:
                    print(voltage)
        value=input()
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()