# Ultrasonic obstacle avoiding Maqueen
# @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)

from microbit import *
import urm10
import utime
urm10 = urm10.URM10(pin1,pin2)
I2caddr = 0x10

# Maqueen motor control
# direction:0=forward  1=back
# speed：0~255
def motor(directionL, speedL, directionR, speedR):
    buf = bytearray(5)
    buf[0] = 0x00
    buf[1] = directionL
    buf[2] = speedL
    buf[3] = directionR
    buf[4] = speedR
    i2c.write(I2caddr, buf)

while True:

# Ultrasonic pin parameters first parameter:Echo,second parameter:Trig
# urm10.read(Echo,Trig)
    a = urm10.read('cm')
    # Exclude invalid ultrasound data
    print(a);

