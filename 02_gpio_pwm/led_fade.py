import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.IN)

pwm = GPIO.PWM(LED_PIN,50)
pwm.start(0)

try:
    for i in range(3):  
        for j in range(0,101,5):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
        for j in range(101,0,-5):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
finally:
    print("cleanup&exit")
    GPIO.cleanup()
    