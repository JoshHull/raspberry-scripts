from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.clear()

f1 = 95
f2 = 205
f3 = 25
while True:
	#if randint(0, 100) == 1:
	#	f1 = randint(0, 15)
	#	f2 = randint(5, 100)
	#	f3 = randint(0, 15)
	pixel_list = sense.get_pixels()

#pixel_list[56] = pixel_list[48]
#pixel_list[48] = pixel_list[40]
#pixel_list[40] = pixel_list[32]
#pixel_list[32] = pixel_list[24]
#pixel_list[24] = pixel_list[16]
#pixel_list[16] = pixel_list[8]
#pixel_list[8] = pixel_list[0]

#print("next interation start")
	for z in range(0,8):
		for i in range(1,8):
			prev=((8)*(8-i))+z
			next=((8)*(7-i))+z
			#print("prev:%d next:%d" % (prev,next))
			pixel_list[prev] = pixel_list[next]

	for w in range(0,8):
		r = randint(0, f1)
		g = randint(0, f3)
		b = randint(0, f2)
		pixel_list[w] = [r,g,b]
	sense.set_pixels(pixel_list)
	sleep(.1)
