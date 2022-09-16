import sys
import time
import board
#import adafruit_dht
import psutil
import requests
from requests.structures import CaseInsensitiveDict
from main import main

url = 'http://192.168.29.184:8080/Iot/Webservices/insertValues.php' 
# We first check if a libgpiod process is running. If yes, we kill it!
for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
#sensor = adafruit_dht.DHT11(board.D23)
while True:

    #temp = sensor.temperature
    weight = main()
    #humidity = sensor.humidity
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "temperature="+str(weight)
    resp = requests.post(url, headers=headers, data=data)
    
    print("Weight: {}% ".format(weight))

        
