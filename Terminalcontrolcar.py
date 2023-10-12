from gpiozero import Motor #Controling DC motors using GPIO
import curses #Controling the car by using terminal

flmotor = Motor(forward=13, backward=17)  #RPIN: 33(GPIO13) & 7 (GPIO4)  Forward = PWM Backward = DIR:
frmotor = Motor(forward=19, backward=4)   #RPIN: 35(GPIO19) & 11(GPIO17) Forward = PWM Backward = DIR:
blmotor = Motor(forward=12, backward=23)  #RPIN: 32(GPIO12) & 15(GPIO22) Forward = PWM Backward = DIR:
brmotor = Motor(forward=18, backward=22)  #RPIN: 12(GPIO18) & 16(GPIO23) Forward = PWM Backward = DIR:

def left():
#    Left 
    flmotor.backward(-1)
    frmotor.forward(1)
    blmotor.backward(-1)
    brmotor.forward(1)

def right():
#    Right 
    flmotor.forward(1)
    frmotor.backward(-1)
    blmotor.forward(1)
    brmotor.backward(-1)

def forward():
#    Forwarding 
    flmotor.forward(1)
    frmotor.forward(1)
    blmotor.forward(1)
    brmotor.forward(1)

def reverse():
#    Reversing 
    flmotor.backward(-1)
    frmotor.backward(-1)
    blmotor.backward(-1)
    brmotor.backward(-1)

def stop():
#    Stopping 
    flmotor.stop(0)
    frmotor.stop(0)
    blmotor.stop(0)
    brmotor.stop(0)

actions = {
    curses.KEY_UP:    forward,
    curses.KEY_DOWN:  reverse,
    curses.KEY_LEFT:  left,
    curses.KEY_RIGHT: right,
}

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
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

curses.wrapper(main)