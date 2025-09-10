from matplotlib import pyplot as plt
import requests

def approximate_line(x,y):
    """
    This is the least square method

    Returns a linear function
    """
    assert len(x) == len(y)
    
    mean_x = sum(x)/len(x)
    mean_y = sum(y)/len(y)

    m = 0

    numerator = 0
    denominator = 0

    # Calculate errors
    for i in range(len(x)):
        numerator += (x[i]-mean_x)*(y[i]-mean_y)
        denominator += (x[i]-mean_x)**2

    k = numerator/denominator
    m = mean_y-k*mean_x

    return lambda x:k*x+m

def plot_data(x,y,title=''):
    """
    Takes raw data and finds a line that fits
    then it plots the data and the line
    """
    f = approximate_line(x,y) # Generate a function

    lx = [i for i in range(min(x),max(x)+1)] # Our x-values
    ly = [f(a) for a in lx] # Calculate y based on the function
    
    plt.plot(x,y,'+') # The original data
    plt.plot(lx,ly) # Fitted line
    plt.title(title) # Set the title
    
    plt.show() # Plots the graph

"""
Här är ett exempel på hur man kan få fram en rät linje
baserat på x- och y-data.

Funktionen plot_data(x,y,titel) ritar ut x- och
y-värdena i ett fönster och drar sen en anpassad linje
till punkterna.

För att få det att fungera använder plot_data
funktionen approximate_line(x,y) som tar emot samma
x- och y-data. Sen räknar den ut funktionen till den
linje som bäst matchar de instoppade värdena. Den
skickar sen tillbaka den funktionen som f(x)=kx+m. Den
funktionen hade gått att använda för att approximera
värden utanför vårt data-utrymme.
"""

##############
## ÖVNING 2 ##
##############
"""
Använd URL:en från exemplet i presentationen och skriv
ut longitud och latitud för Sverige.
"""

##############
## ÖVNING 3 ##
##############
"""
Ändra URL:en och skriv ut longitud och latitud för
Danmark (dk).
"""

##############
## ÖVNING 4 ##
##############
"""
Läs in följande URL som innehåller information om
hushållens sopor i Lund:
https://api.kolada.se/v2/data/municipality/1281/kpi/U07801
Talet 1281 motsvarar Lund.
"""

##############
## ÖVNING 5 ##
##############
"""
Skriv ut värdena i formatet: "årtal: värde"
"""

##############
## ÖVNING 6 ##
##############
"""
Läs in motsvarande data från Helsingborg (1283).
"""

##############
## ÖVNING 7 ##
##############
"""
Vilken kommun samlade in mest sopor per hushåll 2021?
"""

##############
## ÖVNING 8 ##
##############
"""
Hur mycket sopor per hushåll samlas in år 2031?
"""

##############
## ÖVNING 9 ##
##############
"""
Kan kommunerna följa sina trendkurvor i 50 år?
"""

# Notera att datan måste matcha, så att position 0
# båda data-seten måste tillhöra samma punkt.

data_x = [8,2,11,6,5,4,12,9,6,1] # Exempeldata
data_y = [3,10,3,6,8,12,1,4,9,14] # Exempeldata
plot_data(data_x,data_y,'Exempel') # Rita ut exemplet
