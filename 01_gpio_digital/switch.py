import RPi.GPIO as GPIO
import time

SWITCH_PIN = 4
LED_PIN = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN,GPIO.OUT)
try:
    while True:
        val = GPIO.input(SWITCH_PIN)
        GPIO.output(LED_PIN,val)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print("hello?")