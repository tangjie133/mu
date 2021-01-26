#Request husky raw data
from huskylens import *

huskylens.command_knock()
"""
The algorithm includes:
"ALGORITHM_FACE_RECOGNITION"
"ALGORITHM_OBJECT_TRACKING"
"ALGORITHM_OBJECT_RECOGNITION"
"ALGORITHM_LINE_TRACKING"
"ALGORITHM_COLOR_RECOGNITION"
"ALGORITHM_TAG_RECOGNITION"
"ALGORITHM_OBJECT_CLASSIFICATION"
"""
huskylens.command_algorthim("ALGORITHM_FACE_RECOGNITION")

while True:
    data = huskylens.command_request()
    if(data):
        num_of_objects = int(len(data)/5)
        for i in range(num_of_objects):
            x_center = data[5 * i]
            y_center = data[5 * i + 1]
            width    = data[5 * i + 2]
            height   = data[5 * i + 3]
            ID       = data[5 * i + 4]
        print("X_center:", x_center)
        print("Y_center:", y_center)
        print("width:", width)
        print("height:", height)
        print("ID:",ID)


