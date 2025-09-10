from turtle import *

# Innervinkel: 180*(5-2)/5=180*3/5=36*3=90+18=108
# Yttervinkel: 180-108 = 72

speed(0) # Detta gör att allt går skitsnabbt

# polygon

sidor = 0 # Ritade sidor
totala_sidor = 5 # Totala sidor

# vinkelsumma = 180*(totala_sidor-2)
# innervinkel = vinkelsumma/totala_sidor
# yttervinkel = 180-innervinkel

vinkel = 180-180*(totala_sidor-2)/totala_sidor # Beräknad vinkel

# Detta ritar själva polygonen
while sidor < totala_sidor:
    forward(100)
    left(vinkel)
    sidor = sidor+1

    # Detta ritar stjärnorna i hörnen
    spetsar = 0
    totala_spetsar = 5
    while spetsar < totala_spetsar:
        forward(20)
        left(180-180/totala_spetsar)
        spetsar = spetsar+1

# Stjärna

spetsar = 0
totala_spetsar = 5

vinkel = 180-180/totala_spetsar # Beräkna vinkeln

left(360/(totala_spetsar*2)) # Vrid rätt oss

# Rita stjärnan
while spetsar < totala_spetsar:
    fd(160)
    lt(vinkel)
    spetsar = spetsar+1

# Spiral

# Flyttar för syns skull
pu()
bk(100)
pd()

n = 5
while n < 100:
    # Detta flyttar oss mellan stjärnorna
    spetsar = 0
    pu()
    rt(50)
    fd(20+n*2)
    pd()
    # Detta ritar stjärnorna
    while spetsar < n:
        fd(50)
        lt(180-180/n)
        spetsar += 1
    n += 2 # Ser till att vi alltid har udda antal spetsar
    
