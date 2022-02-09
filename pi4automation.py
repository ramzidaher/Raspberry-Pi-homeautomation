import RPi.GPIO as GPIO
from time import sleep
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName == 'off' :
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        pwm=GPIO.PWM(11, 50)
        pwm.start(0)
        pwm.ChangeDutyCycle(5)
        sleep(0.1)
        pwm.stop()
        GPIO.cleanup()
        GPIO.setwarnings(False)
        return render_template ('light_index.html')

    if deviceName == 'on' :
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11, GPIO.OUT)
        pwm=GPIO.PWM(11,50)
        pwm.start(0)
        pwm.ChangeDutyCycle(1.5)
        sleep(0.11)
        pwm.stop()
        GPIO.cleanup()
        GPIO.setwarnings(False)
        return render_template ('light_index.html')
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50, debug=True)

