import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

def Blink(numTimes,speed):
	for i in range(0,numTimes):
		print "Iteration " +str(i+1)
		GPIO.output(4,True)
		time.sleep(speed)
		GPIO.output(4,False)
		time.sleep(speed)
	print "Done"
	GPIO.cleanup()

iterations = raw_input("Enter total numbers of times to blink: ")
speed = raw_input("Enter length of each blink(seconds): ")

Blink(int(iterations),float(speed))