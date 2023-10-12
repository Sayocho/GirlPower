import RPi.GPIO as GPIO
from time import sleep

# Set op GPIO-tilstand (BCM-tilstand bruges i dette eksempel)
GPIO.setmode(GPIO.BCM)

# Declarér pins til højre hjul
RWheel1 = 13        # Forbindelse til PWM signal for højre hjul
RWheelDir2 = 4      # Forbindelse til retningskontrol (skal være "sand" for at køre fremad)
RWheel2 = 19        # Forbindelse til PWM signal for højre hjul
RWheelDir1 = 17     # Forbindelse til retningskontrol (skal være "sand" for at køre fremad)

# Declarér pins til venstre hjul
LWheel1 = 18        # Forbindelse til PWM signal for venstre hjul
LWheelDir2 = 23     # Forbindelse til retningskontrol (skal være "sand" for at køre fremad)
LWheel2 = 12        # Forbindelse til PWM signal for venstre hjul
LWheelDir1 = 22     # Forbindelse til retningskontrol (skal være "sand" for at køre fremad)

# Slå advarsler fra
GPIO.setwarnings(False)

# Opsætning af GPIO pins som output
for pin in [RWheel1, RWheelDir2, RWheel2, RWheelDir1, LWheel1, LWheelDir2, LWheel2, LWheelDir1]:
    GPIO.setup(pin, GPIO.OUT)

# Konfigurer PWM (Pulse Width Modulation) til hjulene
PWM_RWheel1 = GPIO.PWM(RWheel1, 1000)
PWM_RWheel1.start(0)
PWM_RWheel2 = GPIO.PWM(RWheel2, 1000)
PWM_RWheel2.start(0)

PWM_LWheel1 = GPIO.PWM(LWheel1, 1000)
PWM_LWheel1.start(0)
PWM_LWheel2 = GPIO.PWM(LWheel2, 1000)
PWM_LWheel2.start(0)

# Funktion til at ændre retning for højre hjul
def RWheel1_Dir(i):
    GPIO.output(RWheelDir2, i)

# Funktion til at ændre retning for venstre hjul
def LWheel1_Dir(i):
    GPIO.output(LWheelDir2, i)

# Sæt retning til "fremad" for begge hjul
RWheel1_Dir(False)
LWheel1_Dir(False)

while True:
    # Gradvist øge duty cycle for at øge hastigheden (fremad)
    for duty in range(0, 101, 1):
        PWM_RWheel1.ChangeDutyCycle(duty)
        PWM_RWheel2.ChangeDutyCycle(duty)
        PWM_LWheel1.ChangeDutyCycle(duty)
        PWM_LWheel2.ChangeDutyCycle(duty)
        sleep(0.1)

    # Gradvist formindsk duty cycle for at bremse og stoppe
    for duty in range(100, -1, -1):
        PWM_RWheel1.ChangeDutyCycle(duty)
        PWM_RWheel2.ChangeDutyCycle(duty)
        PWM_LWheel1.ChangeDutyCycle(duty)
        PWM_LWheel2.ChangeDutyCycle(duty)
        sleep(0.1)