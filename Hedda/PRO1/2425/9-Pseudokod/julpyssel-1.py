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


"""
Pseudokod till del 1

FOR i IN range(7):
    PRINT " "*(7-i-1)
    PRINT "#"+"##"*i
    PRINT new line
PRINT " "*6 + "|"
"""

"""

Pseudokod till del 2

FOR i IN range(7):
    PRINT " "*(7-i-1)
    FOR j in range(1+2*i):
        r = random.randint(1,5)
        IF r == 1:
            PRINT "o"
        ELSE:
            PRINT "#"
    PRINT new line
PRINT " "*6 + "|"
"""

"""
FOR i IN range(7):
    PRINT " "*(7-i-1)
    FOR j in range(1+2*i):
        r = random.randint(1,5)
        IF r == 1:
            PRINT "o"
        ELSE IF r == 2:
            PRINT "i"
        ELSE:
            PRINT "#"
    PRINT new line
PRINT " "*6 + "|"
"""
