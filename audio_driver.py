
from time import sleep
from linkedList import linkedList
import subprocess
# import serial

state= 'true'
# bluetoothSerial = serial.Serial("/dev/rfcomm1", 9600)

count = 0
prevMaxNoise = 0
myList = linkedList()
def loop (state):
	brown = subprocess.Popen(['mpg321', '/samples/brown.mp3', '-g', '25']);
	sleep(1)
	subprocess.Popen.terminate()
	brown = subprocess.Popen(['mpg321', '/samples/brown.mp3', '-g', '25']);
	#sleep(.5)
	brown.terminate()

#stay at volume for 5 seconds then floor it


# def loop():
# 	global prevMaxNoise
# 	while state == 'true':
# 		print("Checking bluetooth signal")
# 		line = int( bluetoothSerial.readline())
# 		myList.cycle(line)
# 		volume = myList.frontNodeValue()
# 		print "Current Volume %v" % volume
	
loop(state)