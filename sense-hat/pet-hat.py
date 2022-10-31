from sense_hat import SenseHat
import time
sense = SenseHat()
sense.clear()
sense.set_rotation(180) 
p = (204, 0, 204) # Pink
g = (0, 102, 102) #  Dark Green
w = (200, 200, 200) # White
y = (204, 204, 0) # Yellow
e = (0, 0, 0) # Empty

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

def walking():  
    for i in range(9):
        sense.set_pixels(pet1)
        time.sleep(0.5)
        sense.set_pixels(pet2)
        time.sleep(0.5)

x, y, z = sense.get_accelerometer_raw().values()
while True: 
#     while x<1 and y<1 and z<1:      
#          x, y, z = sense.get_accelerometer_raw().values()

     walking()
     sense.clear()

#     x, y, z = sense.get_accelerometer_raw().values()
