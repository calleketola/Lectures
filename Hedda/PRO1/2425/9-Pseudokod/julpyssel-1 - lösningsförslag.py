"""
Använd loopar för att rita ut
följande gran:
      #
     ###
    #####
   #######
  #########
 ###########
#############
      |
Det är sex mellanslag till första
#-symbolen. Samt sex mellanslag
till foten.

Utveckla din kod till att rita ut
julgranskulor också (slumpa ut
kulorna):
      #
     ###
    #o###
   ####o##
  #o#o###o#
 ####o#o##o#
o##o####o####
      |

Granen behöver också ha ljus:
      #
     #i#
    #o###
   #i##o##
  #o#o#i#o#
 #i##o#o##o#
o##o##i#o##i#
      |
"""




# Uppgift 1
for i in range(7):
    print(" "*(7-i-1), end="")
    print("#"+"##"*i,end="")
    print()
print(" "*6+"|")

## Uppgfit 2
import random


for i in range(7):
    print(" "*(7-i-1),end="")
    for j in range(1+2*i):
        r = random.randint(1,5)
        if r == 1:
            print("o",end="")
        else:
            print("#",end="")
    print()
print(" "*6+"|")

## Uppgfit 3
import random
for i in range(7):
    print(" "*(7-i-1),end="")
    for j in range(1+2*i):
        r = random.randint(1,5)
        if r == 1:
            print("o",end="")
        elif r == 2:
            print("i",end="")
        else:
            print("#",end="")
    print()
print(" "*6+"|")
