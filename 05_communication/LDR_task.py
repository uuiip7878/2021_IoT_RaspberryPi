import spidev
import time
import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 100000

def analog_read(channel):
    ret = spi.xfer2([1,(8+channel)<<4,0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out



try:
    while True:
        reading = analog_read(0)
        print("Current read: %d" % reading)
        if reading >= 512:
            GPIO.output(LED_PIN,GPIO.LOW)
        else:
            GPIO.output(LED_PIN,GPIO.HIGH)
        time.sleep(0.5)
finally:
    spi.close()