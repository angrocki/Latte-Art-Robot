

from serial import Serial
import time
import math

points=50
radius=15
x = []
y = []
step_size = 2*math.pi/points
step = 0
for _ in range(points):
    round(math.cos(step) + radius, 2)
    x.append(round(math.cos(step) * radius, 2)) 
    y.append(round(math.sin(step) * radius, 2))
    step = step + step_size 
print(x)
print(y)
