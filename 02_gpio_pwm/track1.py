import RPi.GPIO as GPIO
import threading
import time

BUZZER_PINS = [23,24]
SEGMENT_PINS=[2,3,4,5,6,7,8]
DIGIT_PINS = [10,11,12,13]
BUTTON_PIN = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PINS[0],GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PINS[0],1)
GPIO.setup(BUZZER_PINS[1],GPIO.OUT)
pwm2 = GPIO.PWM(BUZZER_PINS[1],1)
GPIO.setup(BUTTON_PIN,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
for segment in SEGMENT_PINS:
    GPIO.setup(segment,GPIO.OUT)
    GPIO.output(segment,GPIO.LOW)
#자리수 제어는 하이가 오프
for digit in DIGIT_PINS:
    GPIO.setup(digit,GPIO.OUT)
    GPIO.output(digit,GPIO.LOW)
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
sharp = [False,False,False,False,False,False,False]
flat = [False,False,False,False,False,False,False]
melody = [32.7032,36.7081,41.2034,43.6535,48.9994,55,61.7354] # 도,레,미,파,솔,라,시
sharp_melody = [34.6478,38.8909,43.6535,46.2493,51.9130,58.2705,32.7032] # 도#,레#,파(미#),파#,솔#,라#,도
flat_melody = [61.7354,34.6478,38.8909,41.2034,46.2493,51.9130,58.2705]
def note(octave,num,length,array=0,volume=80,offset=0):# 음표 입력 (가운데 도는 4,0)
    if flat[num] is True:
        if num is 1:
            octave=octave-1
        mel = flat_melody[num]*(2**(octave-1))
    if sharp[num] is False:
        if flat[num] is False:
            mel = melody[num]*(2**(octave-1)) #옥타브 설정
    else:
        if num is 6:
            octave=octave+1
        mel = sharp_melody[num]*(2**(octave-1))
    print(mel)
    length = 1.5/length
    time.sleep(offset)
    if array is 0:
        pwm.start(volume)
        pwm.ChangeFrequency(mel)
        time.sleep(length)
        pwm.stop()
    elif array is 1:
        pwm2.start(volume)
        pwm2.ChangeFrequency(mel)
        time.sleep(length)
        pwm2.stop()
def rest(length): #쉼표 입력
    length = 1.5/length
    time.sleep(length)
class col(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name            # thread 이름 지정
    def setnote(self,octave,num,length,volume=80,offset=0):
        self.octave=octave
        self.num=num
        self.length=length
        self.volume=volume
        self.offset=offset
    def run(self):
        note(self.octave,self.num,self.length,1,self.volume,self.offset)

class timer(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        pass #타이머넣어야하는데...ㅠㅠㅠ


flat[2] = True
flat[5] = True
flat[6] = True

def secnote(octave,num,length,volume=80,offset=0):
    c = col("hwaum")
    c.setnote(octave,num,length,volume,offset)
    c.start()

var = False
try:              # 내림마장조는 미,라,시를 각각 레#,솔#,라#로 표기한다. 
    
    while var is not 1:
        var = GPIO.input(BUTTON_PIN)
        print(var)
        time.sleep(0.1)
    
    print("1번 곡")# Plum - R (내림마장조)
    for i in range(4):
        note(5,2,8)#1
        note(5,3,8)
        rest(8)
        note(5,6,8)
        rest(8)
        note(5,3,8)
        rest(8)
        note(5,2,8)
        note(4,5,8)#2
        note(5,2,8)
        rest(8)
        note(5,6,8)
        rest(8)
        note(5,3,8)
        rest(8)
        note(5,2,8)
        note(4,6,8)#3
        note(5,3,8)
        rest(8)
        note(5,6,8)
        rest(8)
        note(5,3,8)
        rest(8)
        note(5,2,8)
        if i is 0 or i is 2:
            rest(8)#4
            note(6,2,8)
            note(6,1,8)
            note(5,6,8)
            rest(8)
            note(5,3,8)
            rest(8)
            note(4,6,8)
        elif i is 1 or i is 3:
            rest(8)#5
            note(6,2,8)
            note(6,1,8)
            note(5,6,8)
            note(6,3,8)
            note(5,6,8)
            note(6,6,8)
            if i is 1:
                note(5,3,8)
            else:
                rest(8)
    note(4,6,4)#6
    note(5,2,4)
    rest(32)
    note(5,2,8)
    note(5,1,8)
    note(5,2,8)
    note(5,3,8)
    rest(32)#7
    note(5,3,4)
    note(5,3,8)
    note(5,4,8)
    note(5,2,4)
    note(5,2,8)
    note(4,6,8)
    note(5,0,4)#8
    note(5,2,4)
    note(5,1,4)
    note(5,0,4)
    rest(32)
    note(5,0,4)#9
    note(5,0,8)
    note(4,6,8)
    rest(32)
    note(4,6,4)
    note(4,6,8)
    rest(32)
    note(4,6,8)
    note(5,0,4)#10
    rest(32)
    note(5,0,4)
    note(5,1,8)
    flat[6]=False
    note(4,6,8)
    note(5,0,8)
    note(5,1,8)
    flat[6]=True
    note(5,3,4)#11
    note(5,3,8)
    note(5,2,16)
    note(5,1,16)
    note(5,2,4)
    rest(32)
    note(5,2,8)
    note(5,3,8)
    flat[4]=True
    note(5,4,4)#12
    note(5,3,8)
    note(5,2,4)
    note(5,3,4)
    note(4,6,8)
    secnote(4,6,8)
    flat[4]=False
    note(5,2,8)#13
    rest(8)
    secnote(4,6,8)
    note(5,1,8)
    rest(32)
    secnote(4,6,8)
    note(5,2,8)
    rest(8)
    secnote(4,6,8)
    note(5,3,8)
    rest(8)
    secnote(4,6,8)
    note(5,3,8)
    note(4,6,4)#14
    note(5,2,4)
    rest(32)
    note(5,2,8)
    note(5,1,8)
    note(5,2,8)
    note(5,3,8)
    rest(32)
    note(5,3,4)#15
    note(5,3,8)
    note(5,4,8)
    note(5,2,4)
    note(5,2,8)
    note(4,6,8)
    secnote(4,5,4)#16
    note(5,0,4)
    note(5,2,4)
    secnote(4,6,4)
    note(5,1,4)
    note(5,0,4)
    rest(32)
    secnote(4,2,4)#17
    note(5,0,4)
    secnote(4,2,8)
    note(5,0,8)
    note(4,6,8)
    rest(32)
    note(4,6,4)
    note(4,6,8)
    rest(32)
    note(4,6,8)
    secnote(4,5,4)#18
    note(5,0,4)
    rest(32)
    note(5,0,4)
    note(5,1,8)
    flat[6]=True
    note(4,6,8)
    note(5,0,8)
    note(5,1,8)
    flat[6]=False
    note(5,3,4)#19
    note(5,3,8)
    note(5,2,16)
    note(5,1,16)
    note(5,2,4)
    rest(32)
    note(5,2,8)
    note(5,3,8)
    flat[4]=True
    note(5,4,8)#20
    note(5,3,8)
    note(5,2,8)
    note(5,3,4)
    rest(32)
    note(5,3,8)
    flat[4]=False
    note(5,4,8)
    note(5,5,8)
    rest(32)
    note(5,5,4)#21
    note(5,5,8)
    note(5,4,16)
    note(5,3,16)
    note(5,4,4)
    rest(8)
    secnote(5,5,16)
    rest(16)
    secnote(5,6,16)
    flat[2] = False
    flat[5] = False
    flat[6] = False
    sharp[0] = True
    sharp[1] = True
    sharp[3] = True
    sharp[4] = True
    sharp[5] = True# B Major
    rest(16)
    note(5,6,4)#22
    note(5,6,8)
    note(5,5,4)
    note(5,5,8)
    note(5,3,4)
    note(5,0,8)#23
    note(4,6,4)
    note(5,3,4)
    note(4,6,8)
    note(5,0,8)
    note(5,1,8)
    note(5,0,16)#24
    note(4,6,16)
    note(4,5,8)
    note(4,3,8)
    note(5,0,16)
    note(4,6,16)
    note(4,5,8)
    note(4,3,8)
    note(5,0,8)
    note(4,6,16)
    note(4,5,16)
    note(4,3,8)#25
    note(6,3,4)
    note(5,5,16)
    note(5,6,16)
    note(6,0,16)
    note(5,6,16)
    note(5,5,16)
    note(5,3,16)
    note(5,0,16)
    note(4,6,16)
    note(4,5,16)
    note(4,3,16)
    note(5,1,4)#26
    note(5,1,8)
    note(6,1,2)
    note(6,0,16)
    note(6,1,16)
    note(6,3,1)#27
    note(5,6,16)
    note(5,5,16)
    note(5,3,8)
    note(5,1,8)
    note(5,6,16)
    note(5,5,16)
    note(5,3,8)
    note(5,1,8)
    note(5,6,16)
    note(5,5,16)
    note(5,3,16)
    note(5,1,16)
    note(5,0,16)#28
    note(4,3,16)
    note(4,5,16)
    note(5,0,16)
    note(5,3,16)
    note(5,0,16)
    note(5,3,16)
    note(5,4,16)
    note(5,5,16)
    note(5,3,16)
    note(5,5,16)
    note(5,6,16)
    note(6,0,16)
    note(5,6,16)
    note(5,5,16)
    note(5,3,16)
    note(5,6,4)#29
    note(5,6,8)
    note(5,5,4)
    note(5,5,8)
    note(5,3,4)
    note(5,0,8)#30
    note(4,6,4)
    note(5,3,4)
    note(4,6,8)
    note(5,0,8)
    note(5,1,8)
    note(5,0,16)#31
    note(4,6,16)
    note(4,5,8)
    note(4,3,8)
    note(5,0,4)
    note(5,3,4)
    note(6,3,2)#32
    secnote(6,5,16)
    note(6,5,16)
    secnote(6,6,16)
    note(6,6,16)
    secnote(6,5,16)
    note(7,0,16)
    secnote(6,3,16)
    note(6,6,16)
    secnote(6,0,16)
    note(6,5,16)
    secnote(5,3,16)
    note(6,3,16)
    secnote(5,0,16)
    note(6,0,16)
    secnote(5,3,16)
    note(5,6,16)
    secnote(5,0,16)
    note(5,5,16)
    secnote(4,5,16)
    note(5,3,16)
    secnote(4,4,8)#33
    note(5,1,16)
    rest(16)
    secnote(4,3,16)
    note(4,4,16)
    secnote(4,4,16)
    rest(16)
    secnote(5,1,8)
    note(5,4,16)
    rest(16)
    secnote(5,3,16)
    note(6,1,16)
    secnote(5,4,16)
    rest(16)
    secnote(6,1,8)
    note(5,1,16)
    rest(16)
    secnote(6,0,16)
    note(5,4,16)
    secnote(6,1,16)
    rest(16)
    secnote(6,4,8)
    note(6,4,16)
    rest(16)
    secnote(6,1,16)
    note(6,1,16)
    note(6,4,16)
    note(6,6,16)#34
    note(6,5,16)
    note(6,3,16)
    note(6,1,16)
    note(6,3,16)
    note(6,1,16)
    note(6,0,16)
    note(5,6,16)
    note(6,0,16)
    note(5,6,16)
    note(5,5,16)
    note(5,3,16)
    note(5,6,16)
    note(5,5,16)
    note(5,3,16)
    note(5,1,16)
    note(5,0,16)#35
    note(5,3,16)
    note(5,0,16)
    note(4,5,16)
    note(6,0,16)
    note(5,5,16)
    note(5,3,16)
    note(5,0,16)
    note(6,3,16)
    note(6,0,16)
    note(5,5,16)
    note(5,3,16)
    note(6,5,16)
    note(6,3,16)
    note(6,0,16)
    note(5,5,16)
    flat[2] = True
    flat[5] = True
    flat[6] = True
    sharp[0] = False
    sharp[1] = False
    sharp[3] = False
    sharp[4] = False
    sharp[5] = False# Eb Major
    note(5,4,16)#36
    note(5,1,16)
    flat[6]=False
    note(4,6,16)
    note(5,1,16)
    note(5,4,16)
    note(5,1,16)
    note(5,4,16)
    note(5,6,16)
    note(6,4,16)
    note(6,3,16)
    note(6,1,16)
    note(5,6,16)
    note(5,4,16)
    note(5,3,16)
    note(5,2,16)
    note(5,1,16)
    flat[6]=True
    for i in range(2):
        note(5,2,4)#37
        note(5,2,8)
        note(5,1,4)
        note(5,1,8)
        note(5,2,4)
        note(4,6,4)
        note(4,6,8)
        note(5,6,4)
        note(5,6,8)
        note(5,2,4)
        note(5,3,4)
        note(5,3,8)
        note(4,6,4)
        note(4,6,8)
        note(5,5,4)
        rest(32)
        note(5,5,4)
        note(5,4,8)
        note(5,3,8)
        note(5,4,4)
        note(5,6,4)
        if i is 0:
            pass
finally:
    GPIO.cleanup()