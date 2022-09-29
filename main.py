from adafruit_servokit import ServoKit

from flask import Flask, render_template, Response, request


kit = ServoKit(channels=16)

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

@app.route('/move/<int:angle>')
def move(angle):  
  kit.servo[0].angle = angel
  return "{{'Angle':{}}}".format(angle)


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
