import RPi.GPIO as GPIO
import library

#   PINS
pin_led_hart = 17
pin_button1 = 18
pin_button2 = 4
pin_button3 = 7
pin_button4 = 9
pin_led_l1 = 21
pin_led_l2 = 20
pin_led_l3 = 16

#   INITILIAZE LIBRARY CLASS
l = library.Library(pin_led_hart, pin_button1, pin_button2, pin_button3, pin_button4, pin_led_l1, pin_led_l2, pin_led_l3)

GPIO.cleanup()