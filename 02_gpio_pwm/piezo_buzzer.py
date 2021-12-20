import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN,GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN,1)
def STOP(a=0.1):
    pwm.stop()
    time.sleep(a)
    pwm.start(10)
pwm.start(10)

melody = [262,294,330,349,392,440,494,523]
def change(a):
    pwm.ChangeFrequency(melody[a])
try:
    print(melody[1])
    for i in range(2):
        change(4)
        time.sleep(0.5)
        STOP()
        change(4)
        time.sleep(0.5)
        STOP()
        change(5)
        time.sleep(0.5)
        STOP()
        change(5)
        time.sleep(0.5)
        STOP()
        change(4)
        time.sleep(0.5)
        STOP()
        change(4)
        time.sleep(0.5)
        STOP()
        change(2)
        time.sleep(1)
        STOP()
        if i is 0:
            change(4)
            time.sleep(0.5)
            STOP()
            change(4)
            time.sleep(0.5)
            STOP()
            change(2)
            time.sleep(0.5)
            STOP()
            change(2)
            time.sleep(0.5)
            STOP()
            change(1)
            time.sleep(1.5)
            STOP(0.5)
        else:
            change(4)
            time.sleep(0.5)
            STOP()
            change(2)
            time.sleep(0.5)
            STOP()
            change(1)
            time.sleep(0.5)
            STOP()
            change(2)
            time.sleep(0.5)
            STOP()
            change(0)
            time.sleep(1.5)
            STOP(0.5)


finally:
    pwm.stop()
    print("cleanup&exit")
    GPIO.cleanup()