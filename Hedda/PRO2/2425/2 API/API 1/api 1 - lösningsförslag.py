from matplotlib import pyplot as plt
import requests

def approximate_line(x,y):
    """
    This is the least square method
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
print('Övning 2\n')
# Hämta datan
request = requests.get('https://api.worldbank.org/v2/country/swe?format=JSON')
# Läs in datan
data = request.json()
# Skriv ut datan
for key in data[1][0]:
  print(key, data[1][0][key])
# Skriv ut longitud, latitud
print("Longitud:", data[1][0]['longitude'])
print("Latitud:", data[1][0]['latitude'])

input("\nTryck enter för att fortsätta...")

##############
## ÖVNING 3 ##
##############
"""
Ändra URL:en och skriv ut longitud och latitud för
Danmark (dk).
"""
print('--------')
print('\nÖvning 3\n')
# Hämta datan
request = requests.get('https://api.worldbank.org/v2/country/dk?format=json')
# Läs in datan
data = request.json()
# Skriv ut datan
for key in data[1][0]:
  print(key, data[1][0][key])
# Skriv ut longitud och latitud
print("Longitud:", data[1][0]['longitude'])
print("Latitud:", data[1][0]['latitude'])

input("\nTryck enter för att fortsätta...")

##############
## ÖVNING 4 ##
##############
"""
Läs in följande URL som innehåller information om
hushållens sopor i Lund:
https://api.kolada.se/v2/data/municipality/1281/kpi/U07801
Talet 1281 motsvarar Lund.
"""

# Läser in datan om Lund
request_lund = requests.get("https://api.kolada.se/v2/data/municipality/1281/kpi/U07801")
data_lund = request_lund.json()

##############
## ÖVNING 5 ##
##############
"""
Skriv ut värdena i formatet: "årtal: värde"
"""
print('--------')
print('\nÖvning 5\n')
# Detta är data för att plotta
x_data = []
y_data = []

print("Lund")

for i in range(len(data_lund['values'])):
    # Detta skriver ut värdena
    print(data_lund['values'][i]['period'], data_lund['values'][i]['values'][0]['value'])
    # Lägger till värdena till vår graf
    x_data.append(data_lund['values'][i]['period'])
    y_data.append(data_lund['values'][i]['values'][0]['value'])

# Plottar en graf med datan
plot_data(x_data,y_data, 'Lund')

# Detta är trendlinjens funktion
lund = approximate_line(x_data, y_data)

##############
## ÖVNING 6 ##
##############
"""
Läs in motsvarande data från Helsingborg (1283).
"""
print('--------')
print('\nÖvning 6\n')
request_hbg = requests.get("https://api.kolada.se/v2/data/municipality/1283/kpi/U07801")
data_hbg = request_hbg.json()

# Detta är data för att plotta
x_data = []
y_data = []

print("Helsingborg")

for i in range(len(data_hbg['values'])):
    # Detta skriver ut värdena
    print(data_hbg['values'][i]['period'], data_hbg['values'][i]['values'][0]['value'])
    # Lägger till värdena till vår graf
    x_data.append(data_hbg['values'][i]['period'])
    y_data.append(data_hbg['values'][i]['values'][0]['value'])

# Plottar en graf med datan
plot_data(x_data,y_data, 'Helsingborg')

# Detta är trendlinjens funktion
hbg = approximate_line(x_data, y_data)

##############
## ÖVNING 7 ##
##############
"""
Vilken kommun samlade in mest sopor per hushåll 2021?
"""
print('--------')
print('\nÖvning 7\n')
# Nu kollar vi vilken kommun som släppte ut mest
if data_lund['values'][-1]['values'][0]['value'] < data_hbg['values'][-1]['values'][0]['value']:
    print("Lund släppte ut minst sopor 2021")
else:
    print("Helsingborg släppte ut minst sopor 2021")

input("\nTryck enter för att fortsätta...")

##############
## ÖVNING 8 ##
##############
"""
Hur mycket sopor per hushåll samlas in år 2031?
"""
print('--------')
print('\nÖvning 8\n')
# Skriver ut värdena framåt
print("År 2032:", lund(2031), "(Lund),",hbg(2031), "(hbg)")

input("\nTryck enter för att fortsätta...")

##############
## ÖVNING 9 ##
##############
"""
Kan kommunerna följa sina trendkurvor i 50 år?
"""
print('--------')
print('\nÖvning 9\n')
print("År 2071:", lund(2071), "(Lund),",hbg(2071), "(hbg)")

input("\nTryck enter för att avsluta...")
