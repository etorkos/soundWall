
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
	while state == 'true':
		fileName = ("samples/brown.mp3")
		bfile = fileName.encode('utf-8')
		volume = random.randint(1,10)*5
		svol = str(volume)
		bvol = svol.encode('utf-8')
		print "Current Volume %s" % volume
		if previous == 0:
			sound = subprocess.Popen(["mpg321", "-R", "-F", "foobar"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
		if volume == previous:
			pass
		previous = volume
		sound.stdin.flush()
		sound.stdin.write(b'LOAD ' + bfile + b'\n')
		sound.stdin.write(b'GAIN ' + bvol + b'\n')
		print sound.stdout.readline();
		sleep(2);
	
loop()
