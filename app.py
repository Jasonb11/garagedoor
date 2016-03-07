from gpiozero import LED, Button
from flask import Flask, jsonify, render_template
from time import sleep
from threading import Lock
from datetime import timedelta

import time

relay = LED(17, initial_value = True)
sensor = Button(27)
app = Flask(__name__)
lock = Lock()
lastStatus = ('open' if not sensor.is_pressed else 'closed', time.time())

def isOpen():
    global lastStatus
    opened = not sensor.is_pressed
    if opened and lastStatus[0] != 'open':
        lastStatus = ('open', time.time())
    elif not opened and lastStatus[0] != 'closed':
        lastStatus = ('closed', time.time())
    return opened

def elapsedTime():
    return str(timedelta(seconds=time.time() - lastStatus[1]))

@app.route('/')
def index():
    global lastStatus
    return render_template('index.html', open=isOpen(), elapsed=elapsedTime())

@app.route('/door', methods=['GET'])
def doorStatus():
    return jsonify(open=not sensor.is_pressed, elapsed=elapsedTime())

@app.route('/door', methods=['POST'])
def toggleRelay():
    with lock:
        relay.off()
        sleep(1)
        relay.on()

    return jsonify(status=relay.is_lit)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
