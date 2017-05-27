import RPi.GPIO as GPIO
from flask import Flask, render_template
import subprocess
import os
import datetime
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def fan(mode):
    GPIO.output(22, mode)
    return




app = Flask(__name__)


@app.route('/')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'Ceiling Fan',
        'time' : timeString
        }
    return render_template('index.html', **templateData)

@app.route("/foff/")
def foff():
    GPIO.output(22, 1)
    return 'OK'

@app.route("/fon/")
def fon():
    GPIO.output(22, 0)
    return 'OK'

@app.route("/loff/")
def loff():
    GPIO.output(21, 1)
    return 'OK'

@app.route("/lon/")
def lon():
    GPIO.output(21, 0)
    return 'OK'

if __name__ == '__main__':
    app.run(port=80, debug=True, host='0.0.0.0')
