import picamera
from time import sleep

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

print()
#start recording using pi camera
camera.start_recording("/home/pi/RaspiCam/demo.h264")
#wait for video to record
camera.wait_recording(10)
#stop recording
camera.stop_recording()
camera.close()
print("video recording stopped")