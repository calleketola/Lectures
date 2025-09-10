
# 4
ålder = input("Hur gammal är du? ")
ålder = int(ålder)


månader = ålder * 12
dagar = ålder*365.25

print("Du har levt i", månader, "månader eller ", dagar, "dagar.")

# 5

år1 = 2024-ålder

print("Du föddes år", år1)

# 6

granne = input("Hur gammal är din granne? ")
granne = int(granne)

gemensam_ålder = granne + ålder

print("Er gemensamma ålder är", gemensam_ålder)

# 7

mål = input("Skriv en ålder ")
mål = int(mål)

år2 = 2024-granne

nått_mål_1 = år1+mål
nått_mål_2 = år2+mål

print("Du fyller", mål, "år", nått_mål_1)
print("Din granne fyller", mål, "år", nått_mål_2)


""" # Detta löser utvecklingen av turtle2
from turtle import *

# Innervinkel: 180*(5-2)/5=180*3/5=36*3=90+18=108
# Yttervinkel: 180-108 = 72

speed(0) # Detta gör att allt går skitsnabbt

# polygon

hörn = 0 # Ritade hörn
totala_hörn = input("Antal hörn på polygonen? ") # Totala hörn
totala_hörn = int(totala_hörn)

# vinkelsumma = 180*(totala_hörn-2)
# innervinkel = vinkelsumma/totala_hörn
# yttervinkel = 180-innervinkel

vinkel = 180-180*(totala_hörn-2)/totala_hörn # Beräknad vinkel

# Detta ritar själva polygonen
while hörn < totala_hörn:
    forward(100)
    left(vinkel)
    hörn = hörn+1

    # Detta ritar stjärnorna i hörnen
    uddar = 0
    totala_uddar = 5
    while uddar < totala_uddar:
        forward(20)
        left(180-180/totala_uddar)
        uddar = uddar+1

# Stjärna

uddar = 0
totala_uddar = input("Antal uddar? ")
totala_uddar = int(totala_uddar)

vinkel = 180-180/totala_uddar # Beräkna vinkeln

left(360/(totala_uddar*2)) # Vrid rätt oss

# Rita stjärnan
while uddar < totala_uddar:
    fd(160)
    lt(vinkel)
    uddar = uddar+1
#"""
