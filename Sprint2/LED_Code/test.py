# # -*- coding: utf-8 -*-
# from serial import Serial, SerialException
# import time
import math

# arduino = Serial(port = '/dev/cu.usbmodem1101', baudrate=115200, timeout=0)
# time.sleep(2)
# while True:
#     line = arduino.readline().decode().rstrip()
#     print(line)
#     # decoded = bytes[0:len(bytes)].decode("utf-8")
#     # print(decoded)
#     if line == '>':
#         message = "M1"
#         # arduino.write(str.encode(">"+message))
#         arduino.write(str.encode(message+"\n"))

#Testing Circle
def make_circle(radius, points): 
    # origin is 0
    x = []
    y = []
    i = 0
    step_size = 2*math.pi/points
    step = 0
    for i in range(points):
        round(math.cos(step) + radius, 2)
        x.append(round(math.cos(step) * radius, 2)) 
        y.append(round(math.sin(step) * radius, 2))
        step = step + step_size 
    return x, y
radius = 50 #mm
points = 10 #number poitns
x, y = make_circle(radius, points)

for i in range(len(x)):
    message = "G1 X{} Y{}\n".format(x[i],y[i])
    print(message)
message = "G1 X{} Y{}\n".format(x[0],y[0])
print(message)
   