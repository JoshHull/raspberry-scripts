from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.clear()
sense.low_light = True
pixel_list = sense.get_pixels()
while True:
	for index in range(1,20,1):
		print("showing G value of ", index)
		sense.clear([0,index,0])
		sleep(.5)
	for index in range(20,1,-1):
		print("showing G value of ", index)
		sense.clear([0,index,0])
		sleep(.5)


for index in range(0,64):
	pixel_list[index][1] = 133 - index * 1

sense.set_pixels(pixel_list)

sleep(2)

for index in range(0,64):
	pixel_list[index][1] = 65 - index * 1

sense.set_pixels(pixel_list)
sleep(2)

