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
        kit.servo[1].angle = ang + 10
        #   kit.continuous_servo[1].throttle = 1
    moveback(ang)
    return "{{'Angle':{}}}".format(angle)

@app.route('/moveback/<int:angle>')
def moveback(angle):
    angle + 90
    for ang in range(90):
        time.sleep(1)
        print(ang)
        kit.servo[1].angle = ang + 10
        #   kit.continuous_servo[1].throttle = 1
    return "{{'Angle':{}}}".format(angle)

@app.route('/move2/<int:angle>')
def move2(angle):
    for ang in range(90):
        time.sleep(1)
        print(ang)
    kit.servo[5].angle = angle
    #   kit.continuous_servo[1].throttle = 1
    return "{{'Angle':{}}}".format(angle)

@app.route("/move3")
async def move3():
    data = await move1(1)
    return "{{'Angle':{}}}".format(1)

@app.route('/move4/<int:angle>')
def move4(ping):
#     for ang in range(90):
#         time.sleep(1)
#         print(ang)
    kit.servo[ping].angle = 0
    time.sleep(ping)
    kit.servo[ping].angle = 20
    time.sleep(ping)
    kit.servo[ping].angle = 40
    time.sleep(ping)
    kit.servo[ping].angle = 60 
    time.sleep(ping)
    kit.servo[ping].angle = 80
    time.sleep(ping)
    kit.servo[ping].angle = 60
    time.sleep(ping)
    kit.servo[ping].angle = 40 
    time.sleep(ping)
    kit.servo[ping].angle = 20 
    time.sleep(ping)
    kit.servo[ping].angle = 0
    
    
    #   kit.continuous_servo[1].throttle = 1
    return "{{'Angle':{}}}".format(ping)


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
