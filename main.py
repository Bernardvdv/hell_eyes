import time 

from adafruit_servokit import ServoKit

from flask import Flask, render_template, Response, request


kit = ServoKit(channels=16)

# App Globals (do not edit)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') #you can customze index.html here

@app.route('/move1/<int:angle>')
def move1(angle):
    for ang in range(90):
        time.sleep(1)
        print(ang)
        kit.servo[1].angle = ang
        #   kit.continuous_servo[1].throttle = 1
    moveback(ang)
    return "{{'Angle':{}}}".format(angle)

@app.route('/moveback/<int:angle>')
def moveback(angle):
    angle + 90
    for ang in range(90):
        time.sleep(1)
        print(ang)
        kit.servo[1].angle = ang
        #   kit.continuous_servo[1].throttle = 1
    return "{{'Angle':{}}}".format(angle)

@app.route('/move2/<int:angle>')
def move2(angle):  
  kit.servo[4].angle = angle
#   kit.continuous_servo[1].throttle = 1
  return "{{'Angle':{}}}".format(angle)


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
