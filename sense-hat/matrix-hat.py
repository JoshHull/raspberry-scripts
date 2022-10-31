from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
sense.set_rotation(180)
sense.clear()
sense.low_light = False
sense.low_light = True

whiteMin=95
brightMax=220
ri=0
gi=1
bi=2
ngFade=55
grFade=25
pixel_list = sense.get_pixels()
letters = [1,5,7]
numLetters=9
#letters = [0,1,2,3,4,5,6,7]
#numLetters=8

while True:

#so the idea is... keep a list of letters.  where the letters is at.  for each screenrefresh, add 8 to each of the letter values in the list. see if you can get one set all the way down the screen.  so what you do is to reduce the brightness of the entire screen, and then after the dimming event, put the letters into the next position.  see if you can do it with a row of every other letter. 

	for index in range(0,64):
		if pixel_list[index][gi] > grFade:
			pixel_list[index][gi] = pixel_list[index][gi]-grFade
		else:
			pixel_list[index][gi] = 0

		if pixel_list[index][ri] > ngFade:
			pixel_list[index][ri] = pixel_list[index][ri]-ngFade   
			pixel_list[index][bi] = pixel_list[index][bi]-ngFade   
		else:
			pixel_list[index][ri] = 0
			pixel_list[index][bi] = 0

	for i in range(len(letters)):
		#make the letters white. And put them on the pixel grid
		#If you make the whites blink bright and dark it will naturally make the greens blink 
		pv=randint(whiteMin,brightMax)
		pixel_list[letters[i]] = [pv,pv,pv]

		#move the letters down one row for the next loop.  Unless they're at the last row, then put them on the top row
		if letters[i] < 56:
			letters[i] = letters[i] + 8 
		else:
			#letters[i] = letters[i] - 56
			letters[i] = randint(0,7)

	#	print(letters)
	if len(letters) < numLetters:
		letters.extend([randint(0,7)])
	#print("next pixel set")
	#print(pixel_list)
	sense.set_pixels(pixel_list)
	sleep(.15)
