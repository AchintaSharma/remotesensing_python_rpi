#! /usr/bin/python2

import time
import sys
from smbus2 import SMBus
from mlx90614 import MLX90614


EMULATE_HX711=False
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)


hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(360.5)


hx.reset()
hx.tare()

print("Tare done! Add weight now...")

while True:
    try:
        val = max(0, int(hx.get_weight(5)));
        print(val)

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
        temp = sensor.get_obj_temp();
        print (temp)


    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
        bus.close()