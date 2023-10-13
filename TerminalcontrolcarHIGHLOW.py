import RPi.GPIO as GPIO
#import sleep #!!!!MAYBE!!!!
import time
import curses

#PWM&GPIO pins to the four engines.

#FRONTLEFT
flPWM = 13    #RPIN33 (GPIO13)
flGPIO = 4    #RPIN7  (GPIO4)
#FRONTRIGHT
frPWM = 19    #RPIN35 (GPIO19)
frGPIO = 17    #RPIN11 (GPIO17)
#BAGLEFT
blPWM = 12    #RPIN32 (GPIO12)
blGPIO = 22   #RPIN15 (GPIO22)
#BAGRIGHT
brPWM = 18    #RPIN12 (GPIO18)
brGPIO = 23   #RPIN16 (GPIO23)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Setting PWM&GPIO the pins as output.
#FRONTLEFT
GPIO.setup(flPWM, GPIO.OUT)
GPIO.setup(flGPIO, GPIO.OUT)
#FRONTRIGHT
GPIO.setup(frPWM, GPIO.OUT)
GPIO.setup(frGPIO, GPIO.OUT)
#BAGLEFT
GPIO.setup(blPWM, GPIO.OUT)
GPIO.setup(blGPIO, GPIO.OUT)
#BAGRIGHT
GPIO.setup(brPWM, GPIO.OUT)
GPIO.setup(brGPIO, GPIO.OUT)


#Right 
def right():
    GPIO.output(flPWM, GPIO.HIGH)
    GPIO.output(flGPIO, GPIO.HIGH)
    GPIO.output(frPWM, GPIO.HIGH)
    GPIO.output(frGPIO, GPIO.LOW)
    GPIO.output(blPWM, GPIO.HIGH)
    GPIO.output(blGPIO, GPIO.HIGH)
    GPIO.output(brPWM, GPIO.HIGH)
    GPIO.output(brGPIO, GPIO.HIGH)
"""
#RightOG
def right():
    GPIO.output(flPWM, GPIO.HIGH)
    GPIO.output(flGPIO, GPIO.HIGH)
    GPIO.output(frPWM, GPIO.LOW)
    GPIO.output(frGPIO, GPIO.LOW)
    GPIO.output(blPWM, GPIO.HIGH)
    GPIO.output(blGPIO, GPIO.HIGH)
    GPIO.output(brPWM, GPIO.LOW)
    GPIO.output(brGPIO, GPIO.LOW)
"""
#Left
def left():
    GPIO.output(flPWM, GPIO.HIGH)
    GPIO.output(flGPIO, GPIO.HIGH)
    GPIO.output(frPWM, GPIO.HIGH)
    GPIO.output(frGPIO, GPIO.LOW)
    GPIO.output(blPWM, GPIO.HIGH)
    GPIO.output(blGPIO, GPIO.HIGH)
    GPIO.output(brPWM, GPIO.HIGH)
    GPIO.output(brGPIO, GPIO.HIGH)

"""
#LeftOG
def left():
    GPIO.output(venstreFor, GPIO.LOW)
    GPIO.output(venstreFGPIO, GPIO.LOW)
    GPIO.output(højreFor, GPIO.HIGH)
    GPIO.output(højreFGPIO, GPIO.HIGH)
    GPIO.output(venstreBag, GPIO.LOW)
    GPIO.output(venstreBGPIO, GPIO.LOW)
    GPIO.output(højreBag, GPIO.HIGH)
    GPIO.output(højreBGPIO, GPIO.HIGH)
"""


#Forward 
def forward():
    GPIO.output(flPWM, GPIO.HIGH)
    GPIO.output(flGPIO, GPIO.LOW)
    GPIO.output(frPWM, GPIO.HIGH)
    GPIO.output(frGPIO, GPIO.LOW)
    GPIO.output(blPWM, GPIO.HIGH)
    GPIO.output(blGPIO, GPIO.LOW)
    GPIO.output(brPWM, GPIO.HIGH)
    GPIO.output(brGPIO, GPIO.LOW)

#Revers 
def revers():
    GPIO.output(flPWM, GPIO.HIGH)
    GPIO.output(flGPIO, GPIO.HIGH)
    GPIO.output(frPWM, GPIO.HIGH)
    GPIO.output(frGPIO, GPIO.HIGH)
    GPIO.output(blPWM, GPIO.HIGH)
    GPIO.output(blGPIO, GPIO.HIGH)
    GPIO.output(brPWM, GPIO.HIGH)
    GPIO.output(brGPIO, GPIO.HIGH)

#Stop
def stop():
    GPIO.output(flPWM, GPIO.LOW)
    GPIO.output(flGPIO, GPIO.LOW)
    GPIO.output(frPWM, GPIO.LOW)
    GPIO.output(frGPIO, GPIO.LOW)
    GPIO.output(blPWM, GPIO.LOW)
    GPIO.output(blGPIO, GPIO.LOW)
    GPIO.output(brPWM, GPIO.LOW)
    GPIO.output(brGPIO, GPIO.LOW)

actions = {
    curses.KEY_UP:    forward,
    curses.KEY_DOWN:  revers,
    curses.KEY_LEFT:  left,
    curses.KEY_RIGHT: right,
}

def main(window): #window = refered to the windows in terminal "curses"
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch() #window = refered to the windows in terminal "curses" #getch = single key"press"
        else:
            key = next_key
            next_key = None
        if key != -1:       #-1 full speed one dirction (1 = full speed the other direction. 0= stop)
            # KEY PRESSED
            curses.halfdelay(3) #Orginal 3
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            stop() #Orginal not comment

curses.wrapper(main) # the ending/ the close down of the "empty" terminal window for controlling

