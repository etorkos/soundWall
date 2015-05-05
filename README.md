Sound Wall, the Raspberry Pi - Arduino sound sensor which only creates ambient noise when it hears loud noises outside

#Software steps: 

1: setup git

2a: download serialPy

2b: configure your usb bluetooth handshake 
with module

3: download MPG321
sudo apt-get -y install mpg321

4: configure sound out of speakers
in terminal run:
lsmod | grep snd_bcm2835

*if file is not found run
sudo modprobe snd_bcm2835

then force it to always load with
cd /etc
sudo nano modules

 /etc/modules: kernel modules to load at boot time.
 This file contains the names of kernel modules that should be
 loaded at boot time, one per line. Lines beginning with "#" are
 ignored. Parameters can be specified after the module name.
 
snd-bcm2835

amixer cset numid=3 1

*credit to raspberrypi-spy.co.uk
http://www.raspberrypi-spy.co.uk/2013/06/raspberry-pi-command-line-audio/