
import datetime
import time
import picamera
from time import sleep
import requests
from requests.structures import CaseInsensitiveDict


def runCamera():
    #create object for PiCamera class
    camera = picamera.PiCamera()
    #set resolution
    camera.resolution = (1024, 768)
    camera.brightness = 60
    camera.start_preview()
    #add text on image
    camera.annotate_text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sleep(2)
    #store image
    # filename = "image" + i;
    file_name = "/home/pi/Desktop/Project1/images/image" + str(time.time()) + ".jpg"
    # /home/pi/Desktop/Project1/images
    print("file name is : " + file_name)
    camera.capture(file_name)
    camera.stop_preview()
    camera.close()
    return file_name



url = 'http://192.168.29.184:8080/tutorial/save_imagetoDB/index2.php'

    
file = runCamera();
print("file name in client side : " + file)
files = {'media': open(file, 'rb')}
requests.post(url, files=files)   
print(files);
time.sleep(2.0)
print("Executed")

