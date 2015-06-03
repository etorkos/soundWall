
from time import sleep
from linkedList import linkedList
import subprocess
import serial

state= 'true'
bluetoothSerial = serial.Serial("/dev/rfcomm1", 9600)

count = 0
myList = linkedList()
# def loop (state):
# 	brown = subprocess.Popen(['mpg321', 'samples/brown.mp3', '-g', '25']);
# 	sleep(1)
# 	brown.terminate()

#stay at volume for 5 seconds then floor it


def loop():
	global prevMaxNoise
	sound = None
	previous = 0
	while state == 'true':
		print("Checking bluetooth signal")
		line = int( bluetoothSerial.readline())
		myList.cycle(line)
		volume = myList.frontNodeValue() * 10
		print "Current Volume %s" % volume
	
		if volume == previous:
			pass
		else:
			command = "samples/brown.mp3"
			previous = volume
			if sound is not None:
				subCommand = "-g %s" %volume
				sound.communicate(input=subCommand)
			else:
				sound = subprocess.Popen(["mpg321"] + command.split(), stdin=subprocess.PIPE)
				
	
loop()
