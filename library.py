import RPi.GPIO as GPIO
import time
import os
from random import randint

class Library(object):

    isGeweestHartR1 = False
    isGeweestHartR2 = False
    isGeweestHartR3 = False
    isGeweestLongenR1 = False
    isGeweestLongenR2 = False
    isGeweestLongenR3 = False
    isGeweestLeverR1 = False
    isGeweestLeverR2 = False
    isGeweestLeverR3 = False
    isGeweestMaagR1 = False
    isGeweestMaagR2 = False
    isGeweestMaagR3 = False

    def __init__(self, pin_led_hart, pin_bStart, pin_bHart, pin_bLong, pin_bLever, pin_bMaag, pin_led_l1, pin_led_l2, pin_led_l3):
        self.pin_led_hart = pin_led_hart
        self.pin_bStart = pin_bStart
        self.pin_bHart = pin_bHart
        self.pin_bLong = pin_bLong
        self.pin_bLever = pin_bLever
        self.pin_bMaag = pin_bMaag
        self.pin_led_l1 = pin_led_l1
        self.pin_led_l2 = pin_led_l2
        self.pin_led_l3 = pin_led_l3
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin_led_hart, GPIO.OUT)
        GPIO.setup(pin_bStart, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pin_bHart, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pin_bLong, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pin_bLever, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pin_bMaag, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(pin_led_l1, GPIO.OUT)
        GPIO.setup(pin_led_l2, GPIO.OUT)
        GPIO.setup(pin_led_l3, GPIO.OUT)

    def audioStart(self):
        os.system('mpg123 start.mp3')

    def audioUitleg(self):
        os.system('mpg123 uitleg.mp3')

    def reset(self):
        self.isGeweestHartR1 = False
        self.isGeweestHartR2 = False
        self.isGeweestHartR3 = False
        self.isGeweestLongenR1 = False
        self.isGeweestLongenR2 = False
        self.isGeweestLongenR3 = False
        self.isGeweestLeverR1 = False
        self.isGeweestLeverR2 = False
        self.isGeweestLeverR3 = False
        self.isGeweestMaagR1 = False
        self.isGeweestMaagR2 = False
        self.isGeweestMaagR3 = False

    def audioReset(self):
        os.system('mpg123 reset.mp3')

    def audioHart(self):
        os.system('mpg123 hart.mp3')

    def audioHartWeetje(self):
        random = randint(1, 3)
        if random == 1 and self.isGeweestHartR1 == False:
            os.system('mpg123 hartR1.mp3')
            self.isGeweestHartR1 = True
        elif random == 2 and self.isGeweestHartR2 == False:
            os.system('mpg123 hartR2.mp3')
            self.isGeweestHartR2 = True
        elif random == 3 and self.isGeweestHartR3 == False:
            os.system('mpg123 hartR3.mp3')
            self.isGeweestHartR3 = True

    def audioLongen(self):
        os.system('mpg123 longen.mp3')

    def audioLongenWeetje(self):
        random = randint(1, 3)
        if random == 1 and self.isGeweestLongenR1 == False:
            os.system('mpg123 longenR1.mp3')
            self.isGeweestLongenR1 = True
        elif random == 2 and self.isGeweestLongenR2 == False:
            os.system('mpg123 longenR2.mp3')
            self.isGeweestLongenR2 = True
        elif random == 3 and self.isGeweestLongenR3 == False:
            os.system('mpg123 longenR3.mp3')
            self.isGeweestLongenR3 = True

    def audioLever(self):
        os.system('mpg123 lever.mp3')

    def audioLeverWeetje(self):
        random = randint(1,3)
        if random == 1 and self.isGeweestLeverR1 == False:
            os.system('mpg123 leverR1.mp3')
            self.isGeweestLeverR1 = True
        elif random == 2 and self.isGeweestLeverR2 == False:
            os.system('mpg123 leverR2.mp3')
            self.isGeweestLeverR2 = True
        elif random == 3 and self.isGeweestLeverR3 == False:
            os.system('mpg123 leverR3.mp3')
            self.isGeweestLeverR3 = True

    def audioMaag(self):
        os.system('mpg123 maag.mp3')

    def audioMaagWeetje(self):
        random = randint(1, 3)
        if random == 1 and self.isGeweestMaagR1 == False:
            os.system('mpg123 maagR1.mp3')
            self.isGeweestMaagR1 = True
        elif random == 2 and self.isGeweestMaagR2 == False:
            os.system('mpg123 maagR2.mp3')
            self.isGeweestMaagR2 = True
        elif random == 3 and self.isGeweestMaagR3 == False:
            os.system('mpg123 maagR3.mp3')
            self.isGeweestMaagR3 = True

    def animatieHart(self):
        for i in range(0, 3):
            GPIO.output(self.pin_led_hart, True)
            time.sleep(0.15)
            GPIO.output(self.pin_led_hart, False)
            time.sleep(0.1)
            GPIO.output(self.pin_led_hart, True)
            time.sleep(0.15)
            # GPIO.output(l.pin_led_hart, True)
            # time.sleep(0.4)
            GPIO.output(self.pin_led_hart, False)
            time.sleep(0.3)
            GPIO.output(self.pin_led_hart, True)
            time.sleep(0.15)
            GPIO.output(self.pin_led_hart, False)
            time.sleep(0.1)
            GPIO.output(self.pin_led_hart, True)
            time.sleep(0.15)
            # GPIO.output(l.pin_led_hart, True)
            # time.sleep(0.4)
            GPIO.output(self.pin_led_hart, False)
            time.sleep(0.55)
            str(i + 1)