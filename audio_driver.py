
from time import sleep
from linkedList import linkedList
import subprocess
# import serial

state= 'true'
# bluetoothSerial = serial.Serial("/dev/rfcomm1", 9600)

count = 0
prevMaxNoise = 0
sound = None
myList = linkedList()
# def loop (state):
# 	brown = subprocess.Popen(['mpg321', 'samples/brown.mp3', '-g', '25']);
# 	sleep(1)
# 	brown.terminate()
# 	brown = subprocess.Popen(['mpg321', 'samples/brown.mp3', '-g', '25']);
# 	sleep(5)
# 	brown.terminate()

#stay at volume for 5 seconds then floor it


def loop():
	global prevMaxNoise
	while state == 'true':
		print("Checking bluetooth signal")
		line = int( bluetoothSerial.readline())
		myList.cycle(line)
		volume = myList.frontNodeValue()
		print "Current Volume %v" % volume
		command = "mpg321 samples/brown.mp3 -g %s" % (volume*6);
		if sound is not None:
			sound.terminate()
		sound = subprocess.Popen(command);
	
loop()