from gpiozero import Motor
from time import sleep
import RPi.GPIO as GPIO

#9: Back left forward
#10: Back Right forward
#11: Back left reverse
#12: Back Right reverse
#16: Front Left Forward
#17: Front Left Reverse
#13: Front Right Reverse
#18: Front Right Forward

#motor = Motor(forward=13, backward=17)


motor1 = Motor(forward=13, backward=17)  
motor2 = Motor(forward=19, backward=4)   
motor3 = Motor(forward=12, backward=23) 
motor4 = Motor(forward=18, backward=22)

motor1.enable()
motor2.enable()
motor3.enable()
motor4.enable()



print('Starting robot')

motor1.forward()
motor2.forward()
motor3.forward()
motor4.forward()
sleep(3)
gpio.output(17,True)
motor1.backward()
motor2.backward()
motor3.backward()
motor4.backward()
sleep(3)