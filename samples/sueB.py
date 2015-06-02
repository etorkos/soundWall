from subprocess import Popen, PIPE, STDOUT

#link https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=74875&p=537588&hilit=%2bmpg321

def speak_now(item,v):
        pplay = Popen(['mpg321', '-R', '-F', 'anyword'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
        filename = (folder + item + ".mp3")
        if (os.path.isfile(filename)):
            bfile = filename.encode('utf-8')
            svol = str(v)
            bvol = svol.encode('utf-8')
            pplay.stdin.write(b'GAIN ' + bvol + b'\n')
            pplay.stdin.write(b'LOAD ' + bfile + b'\n')
            playon = 1
            while playon == 1:
                pleng = pplay.stdout.readline()
                if b'@P' in pleng: playon = 0
                else: playon = 1
        pplay.stdin.write(b'QUIT')
