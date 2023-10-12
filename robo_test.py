'''python code'''
import RPi.GPIO as GPIO
from time import sleep



GPIO.setmode(GPIO.BCM)
'''Dette specificerer RPi pins til at følge "Broadcom SOC channel"... Aka., det definere pins i en bestemt rækkefølge'''



RWheel1 = 13
RWheelDir2 = 4
RWheel2 = 19
RWheelDir1 = 17

LWheel1 = 18
LWheelDir2 = 23
LWheel2 = 12
LWheelDir1 = 22
'''Dette er midlertidige pins. Vi skal have sat dem til det de rigtigt skal være...'''

GPIO.setup(RWheel1, GPIO.OUT)
GPIO.setup(RWheelDir2, GPIO.OUT)
GPIO.setup(RWheel2, GPIO.OUT)
GPIO.setup(RWheelDir1, GPIO.OUT)

GPIO.setup(LWheel1, GPIO.OUT)
GPIO.setup(LWheelDir2, GPIO.OUT)
GPIO.setup(LWheel2, GPIO.OUT)
GPIO.setup(LWheelDir1, GPIO.OUT)



PWM_RWheel1 = GPIO.PWM(RWheel1, 1000)
PWM_RWheel1.start(0)
PWM_RWheel2 = GPIO.PWM(RWheel2, 1000)
PWM_RWheel2.start(0)

PWM_LWheel1 = GPIO.PWM(LWheel1, 1000)
PWM_LWheel1.start(0)
PWM_LWheel2 = GPIO.PWM(LWheel2, 1000)
PWM_LWheel2.start(0)
'''Her sætter vi alle "Wheels" op til at køre med pwm'''

def RWheel1_Dir(i):
    GPIO.output(RWheelDir2, i)
def RWheel2_Dir(i):
    GPIO.output(RWheelDir1, i)
def LWheel1_Dir(i):
    GPIO.output(LWheelDir2, i)
def LWheel2_Dir(i):
    GPIO.output(LWheelDir1, i)
'''Dette siger hvilken retning som hjulene skal dreje...'''



RWheel1_Dir(True)
RWheel2_Dir(True)

LWheel1_Dir(True)
LWheel2_Dir(True)


while True:
    for duty in range(0,101,1):
        PWM_RWheel1.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        PWM_RWheel2.ChangeDutyCycle(duty)
        
        PWM_LWheel1.ChangeDutyCycle(duty)
        PWM_LWheel2.ChangeDutyCycle(duty)
        sleep(0.1)
                
    for duty in range(100,0,-1):
        PWM_RWheel1.ChangeDutyCycle(duty)
        PWM_RWheel2.ChangeDutyCycle(duty)
        PWM_LWheel1.ChangeDutyCycle(duty)
        PWM_LWheel2.ChangeDutyCycle(duty)
        sleep(0.1)