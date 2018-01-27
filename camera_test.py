import picamera
import io
import os

from time import sleep

#from serial import serial


#ser = Serial('/dev/ttyACM0', 9600)


def describe_img(image_url):

    file_name = os.path.join(
        os.path.dirname(__file__),
        image_url)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    
    

camera = picamera.PiCamera()
counter = 0
camera.resolution(720, 720)
camera.start_preview()
while True:
    print 'Capturing image:', counter
    camera.capture('image1.jpg')
    describe_img('image1.jpg')
    counter += 1
camera.stop_preview()