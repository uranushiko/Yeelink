import serial
#from httplib2 import Http
#from SimpleCV import Camera
from time import sleep
#import os

#create a new image
#def createImage():
#	myCamera = Camera(prop_set={'width':320,'height':240})
#	frame=myCamera.getImage()
#	frame.save("image.jpg")

#UApiKey = 'a5e57fe83726c289e58c00530c1f748f'

#huri="http://api.yeelink.net/v1.0/device/2269/sensor/2965/datapoints"
#turi="http://api.yeelink.net/v1.0/device/2269/sensor/2964/datapoints"
#method="POST"
#headers={'U-ApiKey':UApiKey}
#h=Http()

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,19200)
serialFromArduino.flushInput()

while True:
	#send humidity and temperature
	if(serialFromArduino.inWaiting() > 0):
                input = serialFromArduino.readline()
                print(input)
#                s = input.split()
#                if(len(s) == 6):
#                        humidity = s[2]
#                        temperature = s[-1]
#                        hbody="{\"value\":"+humidity+"}"
#                        tbody="{\"value\":"+temperature+"}"
#                        hresp,hcontent=h.request(huri,method,hbody,headers)
#                        tresp,tcontent=h.request(turi,method,tbody,headers)
#create a new image
#	createImage()
#send image by sh
#	os.system("./uploadimage.sh")
	sleep(1)
