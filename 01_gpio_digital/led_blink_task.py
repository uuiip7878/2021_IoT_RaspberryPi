import RPi.GPIO as GPIO
import time

LED_PIN = 4
LED_PIN_G = 6
LED_PIN_Y = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_PIN_G, GPIO.OUT)
GPIO.setup(LED_PIN_Y, GPIO.OUT)
def red(duration,end_wait = False):
    LED_PIN = 4
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("red on")
    time.sleep(duration)
    GPIO.output(LED_PIN,GPIO.LOW)
    print("red off")
    if(end_wait):
        time.sleep(duration)
def yellow(duration,end_wait = False):
    LED_PIN = 5
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("yellow on")
    time.sleep(duration)
    GPIO.output(LED_PIN,GPIO.LOW)
    print("yelow off")
    if(end_wait):
        time.sleep(duration)
def green(duration,end_wait = False):
    LED_PIN = 6
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("green on")
    time.sleep(duration)
    GPIO.output(LED_PIN,GPIO.LOW)
    print("green off")
    if(end_wait):
        time.sleep(duration)
for i in range(10):
    red(0.5,True)
    yellow(0.5,True)
    green(0.5,True)
GPIO.cleanup()