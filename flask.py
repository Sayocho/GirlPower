from flask import Flask
import motor_control_module

app = Flask(__name__)

@app.route('/forward')
def forward():
    motor_control_module.forward()
    return 'Moving forward'

@app.route('/backward')
def backward():
    motor_control_module.backward()
    return 'Moving backward'

@app.route('/left')
def left():
    motor_control_module.left()
    return 'Turning left'

@app.route('/right')
def right():
    motor_control_module.right()
    return 'Turning right'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
