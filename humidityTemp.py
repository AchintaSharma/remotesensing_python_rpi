import time
import board
import adafruit_dht
import psutil


def runHumiTempSensor():
    for proc in psutil.process_iter():
        if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
            proc.kill()
    sensor = adafruit_dht.DHT11(board.D23)
    while True:
        try:
            temp = sensor.temperature
            humidity = sensor.humidity
            return [temp, humidity];
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            sensor.exit()
            raise error
        time.sleep(2.0)