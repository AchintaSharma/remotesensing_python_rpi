
import datetime
import time
import picamera
from time import sleep

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
    file_name = "./images/image" + str(time.time()) + ".jpg"
    print("file name is : " + file_name)
    camera.capture(file_name)
    camera.stop_preview()
    camera.close()
    return file_name