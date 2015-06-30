
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
		volume = random.randint(1,10)*5
		svol = str(volume)
		bvol = svol.encode('utf-8')
		print "Current Volume %s" % volume
		if volume == previous:
			pass
		else:
			previous = volume
			if sound is not None:
				#subCommand = "-g %s" %volume
				#sound.communicate(input=subCommand)
				sound.stdin.write(b'GAIN ' + bvol + b'\n')
				print sound.stdout.readline();
				#sound.stdin.write('GAIN ' + bvol + '\n')
				sleep(2);
			else:
				#sound = subprocess.Popen(["mpg321"] + command.split(), stdin=subprocess.PIPE)
				sound = subprocess.Popen(["mpg321", "-R", "-F", "foobar"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
				fileName = ("samples/brown.mp3")
				bfile = filename.encode('utf-8')
				sound.stdin.write(b'GAIN ' + bvol + b'\n')
				sound.stdin.write(b'LOAD ' + bfile + b'\n')
				print sound.stdout.readline();
				#sound.stdin.write('GAIN ' + bvol + '\n')
	
loop()
