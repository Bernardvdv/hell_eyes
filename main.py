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

@app.route('/move4/<int:servo>/<int:ping>')
def move4(servo, ping):
    ping = 0.5
    kit.servo[servo].angle = 0
#     time.sleep(ping)
    kit.servo[servo].angle = 20
    time.sleep(ping)
    kit.servo[servo].angle = 40
#     time.sleep(ping)
    kit.servo[servo].angle = 60 
    time.sleep(ping)
    kit.servo[servo].angle = 80
    kit.servo[servo].angle = 100
#     time.sleep(ping)
    kit.servo[servo].angle = 120 
    time.sleep(ping)
    kit.servo[servo].angle = 140
#     time.sleep(ping)
    kit.servo[servo].angle = 60
    time.sleep(ping)
    kit.servo[servo].angle = 40 
#     time.sleep(ping)
    kit.servo[servo].angle = 20 
    time.sleep(ping)
    kit.servo[servo].angle = 0
    kit.servo[servo].angle = 20
#     time.sleep(ping)
    kit.servo[servo].angle = 40
    time.sleep(ping)
    kit.servo[servo].angle = 60 
#     time.sleep(ping)
    kit.servo[servo].angle = 80
    
@app.route('/move5/<int:servo>')
def move5(servo):
    ping = 0.05
    
    for i in range(170):
        time.sleep(ping)
        angle = i + 10
        kit.servo[servo].angle = angle
        
    
    
    #   kit.continuous_servo[1].throttle = 1
    return "{{'Angle':{}}}".format(i)


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
