
import requests
from requests.structures import CaseInsensitiveDict
import time
from main import main

url = 'http://192.168.29.184:8080/Iot/Webservices/insertValues.php'

while True:

    headers = {"Content-Type": "application/json; charset=utf-8"}

    data = main()
    print(data)
    resp = requests.post(url, headers=headers, json=data)

    print("Data successfully stored in DB")
    time.sleep(2.0)
