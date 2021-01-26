# RGB
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import neopixel
from random import randint

#neopixel = neopixel.NeoPixel()

# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin15, 4)

while True:
    #Iterate over each LED in the strip

    for pixel_id in range(0, len(np)):
        red = randint(0, 60)
        green = randint(0, 60)
        blue = randint(0, 60)

        # Assign the current LED a random red, green and blue value between 0 and 60
        np[pixel_id] = (red, green, blue)

        # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(100)
