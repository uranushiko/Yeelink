import os
from SimpleCV import Camera

myCamera = Camera(prop_set={'width':320,'height':240})
frame=myCamera.getImage()
frame.save("image.jpg")

os.system("./uploadimage.sh")
