import picamera
import io
import os

from time import sleep

from serial import Serial

from google.cloud import vision
from google.cloud.vision import types


client = vision.ImageAnnotatorClient()

ser = Serial('/dev/ttyACM0', 9600)

ANIMALS = set(['turtle', 'green', 'fish', 'shell', 'animal'])

def describe_image(image_url):


    file_name = os.path.join(os.path.dirname(__file__),image_url)

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
        #label detect here
    image = types.Image(content = content)


    response = client.label_detection(image=image)
    labels = response.label_annotations


    for label in labels:
        if label.description in ANIMALS:
            print "ANIMAL DETECTED, STOPPING"
            ser.write(1)
            return
"""
        for label in labels:
            if label.description in ANIMALS:
                print "ANIMAL DETECTED, STOPPING"
                #ser.write(numba)
                return"""
camera = picamera.PiCamera()
counter = 0
while True:
    print "Capturing image"
    camera.capture('image1.jpg')
    describe_image('image1.jpg')
    counter += 1
