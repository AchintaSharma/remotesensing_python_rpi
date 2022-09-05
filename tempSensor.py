from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

print("ambient temp:")
print (sensor.get_amb_temp())
print("object temp:")
print (sensor.get_obj_temp())
bus.close()

