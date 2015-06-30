
from time import sleep
from linkedList import linkedList
import subprocess
import serial
import random

state= 'true'
#bluetoothSerial = serial.Serial("/dev/rfcomm1", 9600)

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
	fileName = ("samples/brown.mp3")
	bfile = fileName.encode('utf-8')
	sound = subprocess.Popen(["mpg321", "-R", "foobar"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
	sound.stdin.write(b'LOAD ' + bfile + b'\n')
	while state == 'true':
		volume = random.randint(1,10)*5
		if volume == previous:
			pass
		previous = volume	
		svol = str(volume)
		bvol = svol.encode('utf-8')
		print "Current Volume %s" % volume
		#sound.stdin.flush()
		sound.stdin.write(b'GAIN ' + bvol + b'\n')
		print sound.stdout.readline();
		sleep(2);
	
loop()
