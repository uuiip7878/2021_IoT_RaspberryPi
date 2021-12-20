from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 4

display = drivers.Lcd()

try:
    print("Writing to display")
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor,PIN)
        now = datetime.datetime.now()
        print(f"{temperature:.1f}*C, {humidity:.1f}%")
        display.lcd_display_string(now.strftime("%x%X"),1)
        display.lcd_display_string(f"{temperature:.1f}*C, {humidity:.1f}%%",2)
        time.sleep(0.5)
finally:
    print("Cleaning up!")
    display.lcd_clear()