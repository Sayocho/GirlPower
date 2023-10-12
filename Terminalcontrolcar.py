from gpiozero import Motor
import curses

flmotor = Motor(forward=16, backward=17) #rasppin: 36(GPIO16) & 11(GPIO17)
frmotor = Motor(forward=18, backward=13) #rasppin: 12(GPIO18) & 33(GPIO13)
blmotor = Motor(forward=9, backward=11) #rasppin: 21(GPIO9) & 23(GPIO11)
brmotor = Motor(forward=10, backward=12) #rasppin: 19(GPIO10) & 32(GPIO12)

def left():
#    print('Left ...')
    flmotor.backward()
    frmotor.forward()
    blmotor.backward()
    brmotor.forward()

def right():
#    print('Right ...')
    flmotor.forward()
    frmotor.backward()
    blmotor.forward()
    brmotor.backward()

def forward():
#    print('Forwarding ...')
    flmotor.forward()
    frmotor.forward()
    blmotor.forward()
    brmotor.forward()

def reverse():
#    print('Reversing ...')
    flmotor.backward()
    frmotor.backward()
    blmotor.backward()
    brmotor.backward()

def stop():
#    print('Stopping ...')
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
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            stop()

curses.wrapper(main)