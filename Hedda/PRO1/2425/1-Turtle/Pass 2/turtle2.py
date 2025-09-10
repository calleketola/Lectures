from turtle import *

# Innervinkel: 180*(5-2)/5=180*3/5=36*3=90+18=108
# Yttervinkel: 180-108 = 72

# Polygon
sidor = 0

while sidor < 5:
    forward(100)
    left(72)
    sidor = sidor + 1

# Stjärna
spetsar = 0

while spetsar < 5:
    forward(100)
    left(180-180/5)
    spetsar = spetsar + 1
