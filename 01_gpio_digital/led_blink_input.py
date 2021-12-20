import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
while True:
    val = input("1:on, 0:off, 9:exit")
    if val == '1' :
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("led on")
    elif val == '0' :
        GPIO.output(LED_PIN,GPIO.LOW)
        print("led off")
    elif val == '9' :
        break
GPIO.output(LED_PIN,GPIO.LOW)
GPIO.cleanup()
print("clean up and exit")