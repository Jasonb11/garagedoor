from gpiozero import LED, Button
from flask import Flask, jsonify, render_template

relay = LED(17, initial_value = True)
sensor = Button(27)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', open=not sensor.is_pressed)

@app.route('/door', methods=['GET'])
def doorStatus():
    return jsonify(open=not sensor.is_pressed)

@app.route('/door', methods=['POST'])
def toggleRelay():
    relay.toggle()
    return jsonify(status=relay.is_lit)

if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0')
