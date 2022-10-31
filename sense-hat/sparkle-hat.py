from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
f1 = 255
f2 = 255
f3 = 255
while True:
    if randint(0, 100) == 1:
        f1 = randint(0, 255)
        f2 = randint(0, 255)
        f3 = randint(0, 255)
    x = randint(0, 7)
    y = randint(0, 7)
    r = randint(0, f1)
    g = randint(0, f2)
    b = randint(0, f3)
    sense.set_pixel(x, y, r, g, b)
    sleep(0.03*randint(0,9))
    x = randint(0, 7)
    y = randint(0, 7)
    sense.set_pixel(x, y, 0, 0, 0)
    

    
