from sense_hat import SenseHat
import time
from random import randint
class pet8x8():
	#this is the constructor

	p = (204, 0, 204) # Pink
	g = (0, 102, 102) #  Dark Green
	w = (200, 200, 200) # White
	y = (204, 204, 0) # Yellow
	e = (0, 0, 0) # Empty

	def __init__(self):
            self.pet1 = self.buildPet1()
            self.pet2 = self.buildPet2()


	def buildPet1(self):
		p=self.p
		g=self.g
		w=self.w
		y=self.y	
		e=self.e
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
	def buildPet2(self):
		p=self.p
		g=self.g
		w=self.w
		y=self.y	
		e=self.e
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


	def randomize(self):
		self.p = (randint(1,255),randint(1,255),randint(1,255))
		self.g = (randint(1,255),randint(1,255),randint(1,255))
		self.w = (randint(1,255),randint(1,255),randint(1,255))
		self.y = (randint(1,255),randint(1,255),randint(1,255))

		self.pet1=self.buildPet1()
		self.pet2=self.buildPet2()
			
 
	def walking(self,sense):  
		for i in range(9):
			sense.set_pixels(self.pet1)
			time.sleep(0.5)
			sense.set_pixels(self.pet2)
			time.sleep(0.5)


	def rand_walking(self,sense):  
		for i in range(9):
			sense.set_pixels(self.pet1)
			time.sleep(0.5)
			sense.set_pixels(self.pet2)
			time.sleep(0.5)
			self.randomize()


