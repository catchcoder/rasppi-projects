import RPi.GPIO as GPIO
from time import sleep
import subprocess
import os

btn_reboot = 4
btn_shutdown = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_reboot,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn_shutdown,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def reboot(channel):
	subprocess.call(['sudo', 'reboot'])
	print ('reboot')	
def shutdown(channel):
	subprocess.call (['sudo','shutdown','-h','now'])
	print ('shutdown')

GPIO.add_event_detect(btn_reboot, GPIO.FALLING,callback=reboot,bouncetime=500)
GPIO.add_event_detect(btn_shutdown, GPIO.FALLING, callback=shutdown,bouncetime=500)


try:
	while True:	
		#print ("code running")

		sleep (1)


finally:
	GPIO.cleanup()
