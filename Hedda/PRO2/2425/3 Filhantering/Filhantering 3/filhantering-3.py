####################
## ÖVNINGAR 01-05 ##
####################

"""
1. Läs in filen filhantering-3-a.txt
2. Vilket är det största talet i filen?
3. Vilket tal är närmast noll?
4. Vad är medelvärdet av talen?
5. Vad är medianen?
"""



####################
## ÖVNINGAR 06-11 ##
####################

"""
6.  Läs in filen filhantering-3-b.txt
7.  Skriv ut innehållet i filen
8.  Verket saknar fem versr. Lägg till dem i en
    ny fil som heter the-nomad.txt
9.  Vilket ord är vanligast förekommande i hela
    texten?
10. Vilken rad i hela texten är längst?
11. Hur många radre slutar på bosktaven n?
"""


####################
## ÖVNINGAR 12-16 ##
####################

"""
12. Läs in filen filhantering-3-c.txt
13. Använd funktionen least_square för att hitta
    den linjära funktion som passar bäst till datan
14. Vad är y-värdet då x är 461?
15. Vad borde y-värdet vara då x är 5?
16. Vad borde y-värdet vara då x är 6123?
"""


def least_square(x, y):
    """
    x: lista med tal
    y: list amed tal
    ---
    Genererar en linjär trendlinje ohc skickar
    tillbaka koefficienterna k & m
    """
    assert len(x) == len(y) # Kontrollerar att de är lika långa
    n = len(x) # Längden på listan
    xy = 0 # Summan av alla x*y
    x2 = 0 # Summan av alla x^2
    for i in range(n): # Gå igenom alla tal
        xy += x[i]*y[i] # Summera produkterna
        x2 += x[i]*x[i] # Summera kvadraterna
    k = (n*xy-sum(x)*sum(y))/(n*x2-sum(x)**2) # Beräkna k

    x_mean = sum(x)/n # Medel x
    y_mean = sum(y)/n # Medel y

    m = y_mean-x_mean*k # m-värdet

    return [k, m]

