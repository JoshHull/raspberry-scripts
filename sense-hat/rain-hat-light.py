from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

rr = 25
rg = 20 
rb = 205
while True:
	pixel_list = sense.get_pixels()

	for z in range(0,8):
		for i in range(1,8):
			lowr=((8)*(8-i))+z
			higr=((8)*(7-i))+z
			#print("lowr:%d higr:%d" % (lowr,higr))
			pixel_list[lowr] = pixel_list[higr]
			if pixel_list[lowr][2] < 5*i:
				pixel_list[lowr][2] = 0
			else:
				pixel_list[higr] = pixel_list[higr]
				pixel_list[lowr][2] = pixel_list[lowr][2]-5*i

	for w in range(0,8):
		r = randint(0, rr)
		g = randint(0, rg)
		b = randint(55, rb)
		pixel_list[w] = [r,g,b]
	sense.set_pixels(pixel_list)
	sleep(.1)
