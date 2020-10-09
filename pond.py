import RPi.GPIO as GPIO
from gpiozero import MCP3008
import time
from time import perf_counter

upper_limit=10000
lower_limit=1000
GPIO.setmode(GPIO.BOARD)

 #for sensor input
GPIO.setup(8,GPIO.IN)
#for switching motor
GPIO.setup(10,GPIO.OUT)
#for switching valve
GPIO.setup(27,GPIO.out)

def findDepth(data):
    #conver voltage to depth

pot=MCP3008(0)
while True:
    depth = findDepth(pot.value)
    if depth<lower_limit:
        GPIO.output(10,True)
        while(depth<upper_limit-100):
            print(depth)
        GPIO.output(10,False)