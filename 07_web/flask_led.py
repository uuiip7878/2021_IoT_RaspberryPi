from flask import Flask
import RPi.GPIO as GPIO
LED_PIN = 4
LED_PIN_2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(LED_PIN_2,GPIO.OUT)
app = Flask(__name__)
@app.route("/")
def hello():
    return '''
        <p>Hello, Flask!!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a></br>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a></br>
    '''
@app.route("/led/<col>/<cmd>")
def led(col,cmd):
    if cmd == "on":
        if col == "red":
            GPIO.output(LED_PIN, GPIO.HIGH)
        elif col == "blue":
            GPIO.output(LED_PIN_2, GPIO.HIGH)
        return f'''
            <p>{col} LED ON</p>
            <a href="/">Go Home</a>
        '''
    elif cmd == "off":
        if col == "red":
            GPIO.output(LED_PIN, GPIO.LOW)
        elif col == "blue":
            GPIO.output(LED_PIN_2, GPIO.LOW)
        return f'''
            <p>{col} LED OFF</p>
            <a href="/">Go Home</a>
        '''
    else:
        return '''ERROR'''

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()