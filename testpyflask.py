from flask import Flask, render_template
import RPi.GPIO as GPIO
from time import sleep

#Initialize Flask app
app = Flask(name)

#Set up GPIO mode
GPIO.setmode(GPIO.BCM)

#Declare pins for right wheel
RWheel1 = 13
RWheelDir2 = 4
RWheel2 = 19
RWheelDir1 = 17

#Declare pins for left wheel
LWheel1 = 18
LWheelDir2 = 23
LWheel2 = 12
LWheelDir1 = 22

#Disable warnings
GPIO.setwarnings(False)

#Set up GPIO pins as output
for pin in [RWheel1, RWheelDir2, RWheel2, RWheelDir1, LWheel1, LWheelDir2, LWheel2, LWheelDir1]:
    GPIO.setup(pin, GPIO.OUT)

#Configure PWM for the wheels
PWM_RWheel1 = GPIO.PWM(RWheel1, 1000)
PWM_RWheel1.start(0)
PWM_RWheel2 = GPIO.PWM(RWheel2, 1000)
PWM_RWheel2.start(0)

PWM_LWheel1 = GPIO.PWM(LWheel1, 1000)
PWM_LWheel1.start(0)
PWM_LWheel2 = GPIO.PWM(LWheel2, 1000)
PWM_LWheel2.start(0)

#Function to change direction for right wheel
def RWheel1_Dir(i):
    GPIO.output(RWheelDir2, i)

#Function to change direction for left wheel
def LWheel1_Dir(i):
    GPIO.output(LWheelDir2, i)

#Set direction to "forward" for both wheels
RWheel1_Dir(False)
LWheel1_Dir(False)

@app.route('/')
def index():
    return render_template('index.html')
from flask import Flask, render_template
import RPi.GPIO as GPIO
from time import sleep

# Initialize Flask app
#app = Flask(__name__)

@app.route('/<action>')
def control_action(action):
    if action == 'forward':
        RWheel1_Dir(False)
        LWheel1_Dir(False)
        PWM_RWheel1.ChangeDutyCycle(50)
        PWM_RWheel2.ChangeDutyCycle(50)
        PWM_LWheel1.ChangeDutyCycle(50)
        PWM_LWheel2.ChangeDutyCycle(50)
    elif action == 'backward':
        RWheel1_Dir(True)
        LWheel1_Dir(True)
        PWM_RWheel1.ChangeDutyCycle(50)
        PWM_RWheel2.ChangeDutyCycle(50)
        PWM_LWheel1.ChangeDutyCycle(50)
        PWM_LWheel2.ChangeDutyCycle(50)
    elif action == 'left':
        # Add your code to turn left
        pass
    elif action == 'right':
        # Add your code to turn right
        pass
    else:
        PWM_RWheel1.ChangeDutyCycle(0)
        PWM_RWheel2.ChangeDutyCycle(0)
        PWM_LWheel1.ChangeDutyCycle(0)
        PWM_LWheel2.ChangeDutyCycle(0)
    return render_template('index.html')

@app.before_first_request
def setup():
    # Any additional setup code can go here
    pass

@app.teardown_appcontext
def cleanup(exception=None):
    GPIO.cleanup()

if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0')
