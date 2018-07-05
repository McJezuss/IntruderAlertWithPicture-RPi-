import RPi.GPIO as GPIO
import time
import picamera
import pygame
import IntruderAlert

#Constants
WIDTH = 1280
HEIGHT = 1024

#Initialize camera
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = False
camera.brightness = 50


GPIO.setmode(GPIO.BOARD)

#Define pin to circuit
pin_to_circuit = 7

def rc_time(pin_to_circuit):
	count = 0
	
	#Output on pin for
	GPIO.setup(pin_to_circuit, GPIO.OUT)
	GPIO.output(pin_to_circuit, GPIO.LOW)
	
	#Change pin back to output
	GPIO.setup(pin_to_circuit, GPIO.IN)
	
	#Count until pin goes high
	while (GPIO.input(pin_to_circuit) == GPIO.LOW):
		count += 1
	return count

#Catch when script is interrupted
NoIntruder = True
try:
	#Main loop
	while NoIntruder:
		print(rc_time(pin_to_circuit))
		value = rc_time(pin_to_circuit)
		#Loop to take picture
		
		if (value > 1000 and not(value ==0)):
			NoIntruder = False
			print ('Intruder Detected \n Taking a photo')
			camera.capture('Intruders/Intruder.jpg') #Overwrites previous photo
			print('Calling')
			IntruderAlert.sendMail()
			print('Done')
			time.sleep(5)
			
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()	
	

			