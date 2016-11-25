import RPi.GPIO as GPIO
import os
import thread
import time
import library

#   PINS
pin_led_hart = 17
pin_bStart = 26
pin_bHart = 18
pin_bLong = 4
pin_bLever = 7
pin_bMaag = 9
pin_led_l1 = 21
pin_led_l2 = 20
pin_led_l3 = 16

#   LEVENS
currentLife = 3

#   INITILIAZE LIBRARY CLASS
l = library.Library(pin_led_hart, pin_bStart, pin_bHart, pin_bLong, pin_bLever, pin_bMaag, pin_led_l1, pin_led_l2, pin_led_l3)

#   Calculates the new currentLife and sends it to lifeLED
def lifeDown():
    global currentLife
    currentLife = currentLife - 1
    time.sleep(0.2)
    lifeLED(currentLife)

def lifeUp():
    global currentLife
    currentLife = 3
    lifeLED(currentLife)

#   Manages the leds for the amount of lives you have
def lifeLED(currentLife):
    if currentLife == 3:
        GPIO.output(l.pin_led_l3, True)
        GPIO.output(l.pin_led_l2, True)
        GPIO.output(l.pin_led_l1, True)
        print "3"
    elif currentLife == 2:
        os.system('mpg123 leven2.mp3')
        GPIO.output(l.pin_led_l3, False)
        GPIO.output(l.pin_led_l2, True)
        GPIO.output(l.pin_led_l1, True)
        print "2"
    elif currentLife == 1:
        os.system('mpg123 leven1.mp3')
        GPIO.output(l.pin_led_l3, False)
        GPIO.output(l.pin_led_l2, False)
        GPIO.output(l.pin_led_l1, True)
        print "1"
    else:
        os.system('mpg123 dead.mp3')
        GPIO.output(l.pin_led_l3, False)
        GPIO.output(l.pin_led_l2, False)
        GPIO.output(l.pin_led_l1, False)
        time.sleep(5)
        l.reset()
        drFlipper()

def drFlipper():
    state = 0
    while True:
        if state == 0:
            bStart = GPIO.input(l.pin_bStart)
            if bStart is 0:
                l.audioStart()
                state = 1 # Hart leds are on
    
        if state == 1:
            global currentLife
            lifeUp()
            bStart = GPIO.input(l.pin_bStart)
            bHart = GPIO.input(l.pin_bHart)
            bLong = GPIO.input(l.pin_bLong)
            bLever = GPIO.input(l.pin_bLever)
            bMaag = GPIO.input(l.pin_bMaag)
            GPIO.output(l.pin_led_hart, True)
            # if the right button(answer) is pressed
            if bStart is 0:
                l.audioUitleg()
            elif bHart is 0:
                GPIO.output(l.pin_led_hart, False)
                time.sleep(1)
                thread.start_new_thread(l.audioHart, ()) # audio starts
                time.sleep(0.1)
                l.animatieHart() # animation starts while audio is on
                time.sleep(1)
                GPIO.output(l.pin_led_hart, True) # led stays on
                state = 2
            elif bLong is 0:
                l.audioLongenWeetje()
            elif bLever is 0:
                l.audioLeverWeetje()
            elif bMaag is 0:
                l.audioMaagWeetje()
    
        if state == 2:
            bStart = GPIO.input(l.pin_bStart)
            bHart = GPIO.input(l.pin_bHart)
            bLong = GPIO.input(l.pin_bLong)
            bLever = GPIO.input(l.pin_bLever)
            bMaag = GPIO.input(l.pin_bMaag)
            # if the right button(answer) is pressed
            if bLong is 0: 
                l.audioLongen()  # audio starts
                lifeUp()
                time.sleep(0.2)
                state = 3
            # if the wrong button(answer) is pressed
            elif bHart is 0:
                lifeDown()
                l.audioHartWeetje()
            elif bLever is 0:
                lifeDown()
                l.audioLeverWeetje()
            elif bMaag is 0:
                lifeDown()
                l.audioMaagWeetje()
            # button to reset
            elif bStart is 0:
                l.audioReset()
                l.reset()
                state = 1
    
        if state == 3:
            bStart = GPIO.input(l.pin_bStart)
            bHart = GPIO.input(l.pin_bHart)
            bLong = GPIO.input(l.pin_bLong)
            bLever = GPIO.input(l.pin_bLever)
            bMaag = GPIO.input(l.pin_bMaag)
            # if the right button(answer) is pressed
            if bLever is 0:  
                l.audioLever() # audio starts
                lifeUp()
                time.sleep(0.2)
                state = 4
            # if the wrong button(answer) is pressed
            elif bHart is 0: 
                lifeDown()
                l.audioHartWeetje()
            elif bLong is 0:
                lifeDown()
                l.audioLongenWeetje()
            elif bMaag is 0:
                lifeDown()
                l.audioMaagWeetje()
            # button to reset
            elif bStart is 0:
                l.audioReset()
                l.reset()
                state = 1
    
        if state == 4:
            bStart = GPIO.input(l.pin_bStart)
            bHart = GPIO.input(l.pin_bHart)
            bLong = GPIO.input(l.pin_bLong)
            bLever = GPIO.input(l.pin_bLever)
            bMaag = GPIO.input(l.pin_bMaag)
            # if the right button(answer) is pressed
            if bMaag is 0:
                l.audioMaag()
            # if the wrong button(answer) is pressed
            elif bHart is 0:
                lifeDown()
                l.audioHartWeetje()
            elif bLong is 0:
                lifeDown()
                l.audioLongenWeetje()
            elif bLever is 0:
                lifeDown()
                l.audioLeverWeetje()
            # button to reset
            elif bStart is 0:
                l.audioReset()
                l.reset()
                state = 1

drFlipper()