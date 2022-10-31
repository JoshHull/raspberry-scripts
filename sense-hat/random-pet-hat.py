from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()
sense.clear()
sense.set_rotation(180) 
p = (204, 0, 204) # Pink
g = (0, 102, 102) #  Dark Green
w = (200, 200, 200) # White
y = (204, 204, 0) # Yellow
e = (0, 0, 0) # Empty

def randomizepet():
	self.p = (randint(1,255),randint(1,255),randint(1,255))
	self.g = (randint(1,255),randint(1,255),randint(1,255))
	self.w = (randint(1,255),randint(1,255),randint(1,255))
	self.y = (randint(1,255),randint(1,255),randint(1,255))

def buildPet1():

	pet1 = [
	    e, e, e, e, e, e, e, e,
	    p, e, e, e, e, e, e, e,
	    e, p, e, e, p, e, p, e,
	    e, p, g, g, p, y, y, e,
	    e, g, g, g, y, w, y, g,
	    e, g, g, g, g, y, y, e,
	    e, g, e, g, e, g, e, e,
	    e, e, e, e, e, e, e, e
	    ]
	return pet1
def buildPet2():
	pet2 = [
	    e, e, e, e, e, e, e, e,
	    p, e, e, e, e, e, e, e,
	    e, p, e, e, p, e, p, e,
	    e, p, g, g, p, y, y, e,
	    e, g, g, g, y, w, y, g,
	    e, g, g, g, g, y, y, e,
	    e, e, g, e, g, e, e, e,
	    e, e, e, e, e, e, e, e
	    ]

	return pet2

def walking():  
    randomizepet()
    pet1=buildPet1()
    pet2=buildPet2()
    for i in range(5):
        sense.set_pixels(pet1)
        time.sleep(0.5)
        sense.set_pixels(pet2)
        time.sleep(0.5)

#x, y, z = sense.get_accelerometer_raw().values()
while True: 
#     while x<1 and y<1 and z<1:      
#          x, y, z = sense.get_accelerometer_raw().values()
     if randint(0,100) == 1: 
          randomizepet()
     walking()

#     x, y, z = sense.get_accelerometer_raw().values()
