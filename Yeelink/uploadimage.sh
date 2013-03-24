fswebcam -d /dev/video0 -r 320×240 image.jpg
curl --request POST --data-binary @image.jpg --header "U-ApiKey:a5e57fe83726c289e58c00530c1f748f" http://api.yeelink.net/v1.0/device/2269/sensor/2998/photos
