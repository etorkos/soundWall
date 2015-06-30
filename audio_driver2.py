
from time import sleep
from linkedList import linkedList
import subprocess
import serial
import random

state= 'true'
#bluetoothSerial = serial.Serial("/dev/rfcomm1", 9600)

count = 0
myList = linkedList()


def loop():
	previous = 0
	fileName = ("samples/brown.mp3")
	bfile = fileName.encode('utf-8')
	sound.stdin.flush()
	while state == 'true':
		volume = random.randint(1,10)*5
		if volume == previous:
			pass
		previous = volume	
		svol = str(volume)
		bvol = svol.encode('utf-8')
		print "Current Volume %s" % volume
		#sound.stdin.flush()
		sound.stdin.write(b'LOAD ' + bfile + b'\n')
		sound.stdin.write(b'GAIN ' + bvol + b'\n')
		print sound.stdout.readline();
		sleep(2);
	sound.stdin.write(b'QUIT')

try:
	sound = subprocess.Popen(["mpg321", "-R", "foobar"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
	while True:	
		loop()
except KeyboardInterrupt:
	sound.stdin.write(b'QUIT')
