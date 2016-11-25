import RPi.GPIO as GPIO
import library
import time
import os
import thread

#   PINS
pin_led = 17
pin_button1 = 26
pin_button2 = 7
pin_light = 12
pin_ldr = 3

#   INITILIAZE LIBRARY CLASS
l = library.Library(pin_led, pin_button1, pin_button2, pin_light, pin_ldr)

def audio():
    os.system('mpg123 lever.mp3')

#def animation():
    #...

def lever():
    state = 0 #longen is active
    while state is 0:
        input = GPIO.input(l.pin_button1)
        if input is 0: #have to press button to work
            state = 1
            if state is 1:
                GPIO.output(l.pin_led, True)  # LED is on
                time.sleep(1)
                thread.start_new_thread(audio, ())  # audio & animation starts
                #animation()
                time.sleep(1)
                l.lightOn()
                time.sleep(0.2)
                state = 2
        else:
            state = 0
    while state is 2:
        l.life()

while True:
    while l.lightCheck() is 0: #inactive
        time.sleep(0.2)
        l.life()
    while l.lightCheck() is 1: #active
        time.sleep(0.2)
        lever()