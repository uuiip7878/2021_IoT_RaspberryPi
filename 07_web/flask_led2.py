from flask import Flask, render_template
import RPi.GPIO as GPIO
LED_PIN = 4
LED_PIN_2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(LED_PIN_2,GPIO.OUT)
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("led.html")
@app.route("/led/<cmd>")
def led(cmd):
    if cmd == "on":
        GPIO.output(LED_PIN,GPIO.HIGH)
        return "LED ON"
    elif cmd == "off":
        GPIO.output(LED_PIN,GPIO.LOW)
        return "LED OFF"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()