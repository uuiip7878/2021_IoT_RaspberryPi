from flask import Flask, render_template
import RPi.GPIO as GPIO
#red led
LED_PIN = 4
#blue led
LED_PIN_2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(LED_PIN_2,GPIO.OUT)
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("led2.html")
@app.route("/led/<cmd>/<op>")
def led(cmd,op):
    if cmd == "red":
        if op == "on":
            GPIO.output(LED_PIN,GPIO.HIGH)
        elif op == "off":
            GPIO.output(LED_PIN,GPIO.LOW)
    elif cmd == "blue":
        if op == "on":
            GPIO.output(LED_PIN_2,GPIO.HIGH)
        elif op == "off":
            GPIO.output(LED_PIN_2,GPIO.LOW)
    return f"{str.swapcase(cmd)} LED {str.swapcase(op)}"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()