from flask import Flask,render_template
import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

led= 18

gpio.setup(led, gpio.OUT)

app = Flask(__name__)

@app.route('/')
def index():
	#return 'Hello World'
	return render_template('index.html')
@app.route("/led/on")
def led_on():
	gpio.output(led, gpio.HIGH)
	return "LED is ON"
@app.route("/led/off")
def led_off():
	gpio.output(led, gpio.LOW)
	return "LED is OFF"
	

if __name__=='__main__':
	app.run(debug=True,host='0.0.0.0')
