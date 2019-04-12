import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
controls = {
     	1 : {'direction' : 'forward'},
		2 : {'direction' : 'stop'},
		3 : {'direction' : 'right'},
		4 : {'direction' : 'left'}}

GPIO.setmode(GPIO.BCM)

GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

GPIO.output(9,0)
GPIO.output(10,0)
GPIO.output(17,0)
GPIO.output(22,0)
GPIO.output(23,0)
GPIO.output(24,0)
GPIO.output(25,0)
GPIO.output(21,0)

@app.route("/")
def main():
	templateData = {
	   		'controls' : controls
	  	  }
	return render_template('main.html',**templateData)

@app.route("/<action>")
def action(action):
	if action == "forward":
		GPIO.output(22,1)
		GPIO.output(23,1)
		GPIO.output(24,0)
		GPIO.output(25,0)
	if action == "stop":
		GPIO.output(22,0)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(25,0)
	if action == "left":
		GPIO.output(22,1)
		GPIO.output(23,0)
		GPIO.output(24,0)
		GPIO.output(25,0)
	if action == "right":
		GPIO.output(22,0)
		GPIO.output(23,1)
		GPIO.output(24,0)
		GPIO.output(25,0)
	if action == "reverse":
		GPIO.output(22,0)
		GPIO.output(23,0)
		GPIO.output(24,1)
		GPIO.output(25,1)
	templateData = {
 	  'controls' : controls
		}
	return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='localhost',port=8000,debug=False)
