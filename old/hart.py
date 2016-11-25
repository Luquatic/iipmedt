import RPi.GPIO as GPIO
import os
import thread
import time
import library

#   PINS
pin_led = 17
pin_button1 = 26
pin_button2 = 7
pin_light = 12
pin_ldr = 3

#   INITILIAZE LIBRARY CLASS
l = library.Library(pin_led, pin_button1, pin_button2, pin_light, pin_ldr)

def audio():
    os.system('mpg123 hart.mp3')

def animation():
    for i in range(0,3):
        GPIO.output(l.pin_led, True)
        time.sleep(0.15)
        GPIO.output(l.pin_led, False)
        time.sleep(0.1)
        GPIO.output(l.pin_led, True)
        time.sleep(0.15)
        #GPIO.output(l.pin_led, True)
        #time.sleep(0.4)
        GPIO.output(l.pin_led, False)
        time.sleep(0.3)
        GPIO.output(l.pin_led, True)
        time.sleep(0.15)
        GPIO.output(l.pin_led, False)
        time.sleep(0.1)
        GPIO.output(l.pin_led, True)
        time.sleep(0.15)
        #GPIO.output(l.pin_led, True)
        #time.sleep(0.4)
        GPIO.output(l.pin_led, False)
        time.sleep(0.55)
        str(i + 1)

def heartbeat():
    state = 0 #LED is on
    while state is 0:
          input = GPIO.input(l.pin_button1)
          if input == 1: #have to press button to work
                GPIO.output(l.pin_led, True)
                state = 0
          else:
                GPIO.output(l.pin_led, False)
                state = 1
                if state is 1:
                    GPIO.output(l.pin_led, False)
                    time.sleep(1)
                    thread.start_new_thread(audio,()) #audio & animation starts
                    time.sleep(0.1)
                    animation()
                    time.sleep(1)
                    l.lightOn()
                    GPIO.output(l.pin_led, True) #LED stays on but doesn't go back to state 0 to run loop again

heartbeat()
