import RPi.GPIO as GPIO
import time

SWITCH_PIN_1 = 4
SWITCH_PIN_2 = 5
SWITCH_PIN_3 = 6
LED_PIN_R = 3
LED_PIN_Y = 2
LED_PIN_G = 10
GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN_R,GPIO.OUT)
GPIO.setup(LED_PIN_Y,GPIO.OUT)
GPIO.setup(LED_PIN_G,GPIO.OUT)
try:
    while True:
        val = GPIO.input(SWITCH_PIN_1)
        val2 = GPIO.input(SWITCH_PIN_2)
        val3 = GPIO.input(SWITCH_PIN_3)
        GPIO.output(LED_PIN_R,val)
        GPIO.output(LED_PIN_Y,val2)
        GPIO.output(LED_PIN_G,val3)
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print("hello?")