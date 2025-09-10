###############
## ÖVNING 01 ##
###############

"""
Skriv ut följande mönster:

¤#########
#¤########
##¤#######
###¤######
####¤#####
#####¤####
######¤###
#######¤##
########¤#
#########¤
"""


###############
## ÖVNING 02 ##
###############

"""
Utveckla mönstret till:

¤########¤
#¤######¤#
##¤####¤##
###¤##¤###
####¤¤####
####¤¤####
###¤##¤###
##¤####¤##
#¤######¤#
¤########¤
"""




###############
## ÖVNING 03 ##
###############

"""
Gör följande utskrift i fönstret:

1*1 = 1 	1*2 = 2 	1*3 = 3 	
2*1 = 2 	2*2 = 4 	2*3 = 6 	
3*1 = 3 	3*2 = 6 	3*3 = 9 	
4*1 = 4 	4*2 = 8 	4*3 = 12 	
5*1 = 5 	5*2 = 10 	5*3 = 15 	
6*1 = 6 	6*2 = 12 	6*3 = 18 	
7*1 = 7 	7*2 = 14 	7*3 = 21 	
8*1 = 8 	8*2 = 16 	8*3 = 24 	
9*1 = 9 	9*2 = 18 	9*3 = 27 	
10*1 = 10 	10*2 = 20 	10*3 = 30
"""


###############
## ÖVNING 04 ##
###############

"""
Skriv ett program som beräknar summan av
1/1+1/2+1/4+1/8... fram tills den sista
termen är mindre än 0.000001.
"""



###############
## ÖVNING 05 ##
###############

"""
Gör samma som i fyra men med alternerande
tecken, varannan positiv och varannan
negativ. 1/1-1/2+1/4-1/8...
"""

###############
## ÖVNING 06 ##
###############

"""
Vid simhoppstävlingar dömer minst tre domare
som ger poäng från 0 till 10. Man tar bort
den högsta och lägsta poängen och beräknar
medelvärdet av de resterande poängen. Sedan
tar man medelvärdet multiplicerat med 3 och
multiplicerat med hoppets svårighetsgrad för
att få slutpoängen.

Skriv ett program som gör detta. Det ska kräva
att det är minst tre domare, men kunna vara
godtyckligt många. Ta bort det högsta och det
lägsta resultatet och sedan ta medelvärdet.
Multiplicera medelvärdet med tre och hoppets
svårighetsgrad.
"""

###############
## ÖVNING 07 ## # Toksvår
###############

"""
Två-dimensionella objekt brukar indexeras på
följande vis:
a_rk

|a_00 a_01 a_02|
|a_10 a_11 a_12|
|a_20 a_21 a_22|

|a_0 a_1 a_2|
|a_3 a_4 a_5|
|a_6 a_7 a_8|

Skriv en kod som kan identifiera varje element
i den tvådimensionella matrisen med ett
indextal. Koden ska ta emot ett tal mellan 0 och
8 och spotta ut två tal som motsvarar raden och
kolumnen i.e. i = 5 ) (1; 2). Få den att klara av
n x m-objekt (n rader och m kolumner).

Gör en kod som går på
andra hållet. Från rad och kolumn till i.

|31 14 42|
|29 93 77|
|55 88 66|


a_00 = 31 = a_0;
a_11 = 93 = a_4;
a_22 = 66 = a_8
"""

print("Uppgift 7")
matris_2 = [[31,14,42],
            [29,93,77],
            [55,88,66]]
matris_1 = [31,14,42,29,93,77,55,88,66]

# Den här biten kod skriver ut matrisen "snyggt"
for i in range(len(matris_2)): # Varje rad
    print("|", end=" ")
    for j in range(len(matris_2[i])): # Varje kolumn
        print(matris_2[i][j], end=" ")
    print("|")




