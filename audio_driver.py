
from time import sleep
import subprocess
import serial

state= 'true'
bluetoothSerial = serial.Serial("/dev/rfcomm1", 9600)

count = 0
prevMaxNoise = 0

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
		print(line)
		if line >= prevMaxNoise:
			count= 0
			prevMaxNoise = line
			print "volume increases"
		elif count < 8:
			count = count + 1
		else:
			count = 0
			prevMaxNoise = line
	
loop()
