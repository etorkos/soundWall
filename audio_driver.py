
from time import sleep
from linkedList import linkedList
import subprocess
# import serial

state= 'true'
# bluetoothSerial = serial.Serial("/dev/rfcomm1", 9600)

count = 0
prevMaxNoise = 0
myList = linkedList()
#def loop (state):
	#white = subprocess.Popen(['play', '-n', 'synth', 'whitenoise'], stdin=subprocess.PIPE);
	#sleep(.5)
	#subprocess.Popen.terminate()
	#white = subprocess.Popen(['play', '-n', 'synth', 'whitenoise']);
	#sleep(.5)
	#white.terminate()

#stay at volume for 5 seconds then floor it


def loop():
	global prevMaxNoise
	while state == 'true':
		print("Checking bluetooth signal")
		line = int( bluetoothSerial.readline())
		myList.cycle(line)
		volume = myList.frontNodeValue()
		print "Current Volume %v" % volume
	
loop()