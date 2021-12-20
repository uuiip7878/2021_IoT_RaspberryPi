import RPI.GPIO as GPIO
import threading
import time

SEGMENT_PINS=[2,3,4,5,6,7,8]
DIGIT_PINS = [10,11,12,13]
SWITCH_PIN_LOOP = 14
SWITCH_PIN_PLAY = 15
SWITCH_PIN_TRACK = [16,17]
SWITCH_PINS = [14,15,16,17]
BUZZER_PINS = [23,24]
current_track = 0
loop_ONLY = False
loop_TRACK = False


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PINS[0],GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PINS[0],1)
GPIO.setup(BUZZER_PINS[0],GPIO.OUT)
pwm2 = GPIO.PWM(BUZZER_PINS[0],1)
for segment in SEGMENT_PINS:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,GPIO.LOW)
#자리수 제어는 하이가 오프
for digit in DIGIT_PINS:
    GPIO.setup(digit,GPIO.OUT)
    GPIO.output(digit,GPIO.LOW)
for switch in SWITCH_PINS:
    GPIO.setup(switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9
melody = [32.7,36.7,41.2,43.7,49.0,55,61.7]
def note(octave,num,length,array=0,offset=0):# 음표 입력
    mel = melody[num]*(2**(octave-1)) #옥타브 설정
    length = 1000/length
    time.sleep(offset)
    if array is 0:
        pwm.start(10)
        pwm.ChangeFrequency(mel)
        time.sleep(length)
        pwm.stop()
    elif array is 1:
        pwm2.start(10)
        pwm2.ChangeFrequency(mel)
        time.sleep(length)
        pwm2.stop()
def rest(length): #쉼표 입력
    length = 1000/length
    time.sleep(length)
def display(digit,number):
    for i in range(4):
        if i +1==digit:
            GPIO.output(DIGIT_PINS[i],GPIO.LOW)
        else:
            GPIO.output(DIGIT_PINS[i],GPIO.HIGH)
    #숫자 출력
    for i in range(7):
        GPIO.output(SEGMENT_PINS[i],data[number][i])
    time.sleep(0.1)

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정

    def run(self):
        while(True):
            var = GPIO.input(SWITCH_PIN_LOOP)
            if var is 1:
                loop()
    def update(self):
        while(True):
            True = True



try:
    while True:
        True=True
    
finally:
    GPIO.cleanup()