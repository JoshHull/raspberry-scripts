from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
print("Temperature: %s C" % temp)
temp = sense.get_temperature_from_humidity()
print("Huditemp   : %s C" % temp)
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

orientation_rad = sense.get_orientation_radians()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))

orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

north = sense.get_compass()
print("Compass:")
print("North: %s" % north)

raw = sense.get_compass_raw()
print("Compass Raw:")
print("x: {x}, y: {y}, z: {z}".format(**raw))

gyro_only = sense.get_gyroscope()
print("Gyroscope:")	
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

raw = sense.get_gyroscope_raw()
print("Gyroscope Raw:")
print("x: {x}, y: {y}, z: {z}".format(**raw))


# alternatives
print(sense.temp)
print(sense.temperature)
