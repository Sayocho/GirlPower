from gpiozero import Motor #Controling DC motors using GPIO
import curses #Controling the car by using terminal

flmotor = Motor(forward=13, backward=17)  #RPIN: 33(GPIO13) & 7 (GPIO4)  Forward = PWM Backward = DIR:
frmotor = Motor(forward=19, backward=4)   #RPIN: 35(GPIO19) & 11(GPIO17) Forward = PWM Backward = DIR:
blmotor = Motor(forward=12, backward=23)  #RPIN: 32(GPIO12) & 15(GPIO22) Forward = PWM Backward = DIR:
brmotor = Motor(forward=18, backward=22)  #RPIN: 12(GPIO18) & 16(GPIO23) Forward = PWM Backward = DIR:

"""
flmotor = Motor(forward=17, backward=13)
frmotor = Motor(forward=4,  backward=19)
blmotor = Motor(forward=23, backward=12)
brmotor = Motor(forward=22, backward=18)

"""
def left():
#    Left 
    flmotor.backward()
    frmotor.forward()
    blmotor.backward()
    brmotor.forward()

def right():
#    Right 
    flmotor.forward()
    frmotor.backward()
    blmotor.forward()
    brmotor.backward()

def forward():
#    Forwarding 
    flmotor.forward()
    frmotor.forward()
    blmotor.forward()
    brmotor.forward()

def reverse():
#    Reversing 
    flmotor.backward()
    frmotor.backward()
    blmotor.backward()
    brmotor.backward()

def stop():
#    Stopping 
    flmotor.stop()
    frmotor.stop()
    blmotor.stop()
    brmotor.stop()

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
            key = window.getch() #window = refered to the windows in terminal "curses" #getch = single key"press"
        else:
            key = next_key
            next_key = None
        if key != -1:       #-1 full speed one dirction (1 = full speed the other direction. 0= stop)
            # KEY PRESSED
            curses.halfdelay(1) #Orginal 3
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            stop() #Orginal not comment

curses.wrapper(main) # the ending/ the close down of the "empty" terminal window for controlling