#! /usr/bin/python2

import time
import sys
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

EMULATE_HX711=False

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

hx = HX711(5, 6)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(360.5)

hx.reset()
print("Taring, please wait...")
hx.tare()

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
    sys.exit()

def runLoadSensor():
    i = 0;
    load = 0;
    while i < 5: 
        try:
            val = max(0, int(hx.get_weight(5)));
            # val = hx.get_weight(5);
            load += val;
            hx.power_down()
            hx.power_up()
            time.sleep(0.1)
            i += 1;

        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()

    return load/5;