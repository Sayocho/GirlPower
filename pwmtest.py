#PWM test






import RPi.GPIO as GPIO
from time import sleep

SpeedPin = 33
SpeedPin1 = 35
# PWM pins


SpeedPinA = 12
SpeedPinA1 = 32

DirectionPin = 16
DirectionPin1 = 18

DirectionPinA = 11
DirectionPinA1 = 13

GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)	#set pin numbering system

GPIO.cleanup()

GPIO.setup(SpeedPin,GPIO.OUT)
GPIO.setup(SpeedPin1,GPIO.OUT)

GPIO.setup(SpeedPinA,GPIO.OUT)
GPIO.setup(SpeedPinA1,GPIO.OUT)

GPIO.setup(DirectionPin,GPIO.OUT)
GPIO.setup(DirectionPin1,GPIO.OUT)

GPIO.setup(DirectionPinA,GPIO.OUT)
GPIO.setup(DirectionPinA1,GPIO.OUT)


pi_pwm = GPIO.PWM(SpeedPin,1000)		#create PWM instance with frequency
pi_pwm.start(0)

pi_pwm1 = GPIO.PWM(SpeedPin1,1000)		#create PWM instance with frequency
pi_pwm1.start(0)	

pi_pwm1 = GPIO.PWM(SpeedPinA,1000)		#create PWM instance with frequency
pi_pwm1.start(0)

pi_pwm1 = GPIO.PWM(SpeedPinA1,1000)		#create PWM instance with frequency
pi_pwm1.start(0)

GPIO.output(DirectionPin, True)
GPIO.output(DirectionPin1, True)

GPIO.output(DirectionPinA, True)
GPIO.output(DirectionPinA1, True)


#start PWM of required Duty Cycle 
while True:
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        pi_pwm1.ChangeDutyCycle(duty)
        sleep(0.1)
                
    for duty in range(100,0,-1):
        pi_pwm.ChangeDutyCycle(duty)
        pi_pwm1.ChangeDutyCycle(duty)
        sleep(0.1)
