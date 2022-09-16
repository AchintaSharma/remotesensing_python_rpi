import time
import board
#import adafruit_dht
import psutil
import requests
from requests.structures import CaseInsensitiveDict

url = '192.168.29.184:8080/Iot/Webservices/insertTemp.php'
#
#sensor = adafruit_dht.DHT11(board.D23)

        #temp = sensor.temperature
        #humidity = sensor.humidity
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"
data = "temperature= 32"
resp = requests.post(url, headers=headers, data=data)
        
        