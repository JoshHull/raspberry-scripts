from sense_hat import SenseHat
from pet8x8 import pet8x8
import time

sense = SenseHat()
sense.clear()
sense.set_rotation(180) 

pet=pet8x8()
#x, y, z = sense.get_accelerometer_raw().values()
while True: 
#     while x<1 and y<1 and z<1:      
#          x, y, z = sense.get_accelerometer_raw().values()
	pet.rand_walking(sense)
#	pet.randomize()
#     x, y, z = sense.get_accelerometer_raw().values()
