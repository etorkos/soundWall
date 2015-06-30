
from time import sleep
from linkedList import linkedList
import subprocess
import serial
import random
import time

state= 'true'
fileName = ("samples/brown.mp3")
bfile = fileName.encode('utf-8')

def loop():
	previous = 0
	sound.stdin.flush()
	volume = random.randint(1,10)*5
	if volume == previous:
		pass
	previous = volume	
	svol = str(volume)
	bvol = svol.encode('utf-8')
	print "Current Volume %s" % volume
	sound.stdin.write(b'LOAD ' + bfile + b'\n')
	sound.stdin.write(b'GAIN ' + bvol + b'\n')
	print sound.stdout.readline();
	sleep(2);

try:
	start = time.monotonic()
	sound = subprocess.Popen(["mpg321", "-R", "foobar"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
	while True:	
		if time.monotonic() - start < 1700:
			loop()
		else:
			start = time.monotonic()
			sound.terminate()
			sound = subprocess.Popen(["mpg321", "-R", "foobar"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
			loop()

except KeyboardInterrupt:
	sound.stdin.write(b'QUIT')
