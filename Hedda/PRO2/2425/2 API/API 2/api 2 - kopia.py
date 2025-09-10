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

def plot_data(x,y,title=""):
    """
    Takes raw data and finds a line that fits
    then it plots the data and the line
    """
    f = approximate_line(x,y)

    lx = [i for i in range(min(x),max(x)+1)]
    ly = [f(a) for a in lx]
    
    plt.plot(x,y,'+') # The original data
    plt.plot(lx,ly) # Fitted line
    plt.show()

def plot_data_multiple(x,y, cities, title=""):
    """
    Takes raw data and finds a line that fits
    then it plots the data and the line
    """
    colours = 'bgrcmyk' # Färgerna på våra linjer

    # Härifrån kommer du att behöva loopa. Ner till nästa ensamma kommentarsrad
    
    f = approximate_line(x[0],y[0]) # Skapar den räta linjen

    lx = [i for i in range(min(x[0]),max(x[0])+1)] # Skapar alla x-värden
    ly = [f(a) for a in lx] # Räknar ut motsvarande y-värden
        
    plt.plot(x[0],y[0],'+'+colours[0], label=c_names[cities[0]]) # The original data
    plt.plot(lx,ly, colours[0], label=c_names[cities[0]]) # Fitted line

    # Här ska din loop sluta. 

    plt.title(title)
    plt.legend() # Lägger till "färgbeskrivning"
    plt.show() # Visar grafen

# keys = ['N45900','N45905','N45912','N45920']
# nycklarnas betydelse:
# 'N45900': "Elpris inkl. moms för typfastighet enligt Nils Holgersson-modellen, kr/kvm"
# 'N45905': "Slutanvändning av energi totalt inom det geografiska området, MWh/inv"
# 'N45912': "Slutanvändning energi inom offentlig verksamhet inom det geografiska området, MWh/inv"
# 'N45920': "Slutanvändning energi inom hushåll inom det geografiska området, MWh/inv"

keys = {'N45900': "Elpris inkl. moms kr/kvm",
        'N45905': "Slutanvändning av energi totalt",
        'N45912': "Slutanvändning energi inom offentlig verksamhet",
        'N45920': "Slutanvändning energi inom hushåll"}

# Listor för att hålla vår data
kpi = ['N45900'] # En lista med nycklar
c_names = {1280: "Malmö",
           1281: "Lund",
           1282: "Landskrona",
           1283: "Helsingborg",
           1284: "Höganäs",
           1285: "Eslöv"}

#################################################
#################################################

# Här nedanför börjar du innan du fixar i plot_data_multiple 

data = [] # Informationen vi laddar ner
cities = [1281] # En lista med kommunkoder. Den här behöver du fylla

# Hämtar datan och gör om till JSON-format. Här kommer du att behöva en loop
request = requests.get('https://api.kolada.se/v2/data/municipality/{}/kpi/{}'.format(cities[0], kpi[0]))
data.append(request.json())

x = [[] for i in range(len(data))] # Lista med tomma listor till våra x-värden (årtal)
y = [[] for i in range(len(data))] # Lista med tomma listor till våra y-värden (värde)

# Append all the values
# Detta fixar för EN graf. Du behöver Lägga till en yttre loop som loopar igenom alla data-set
for i in range(len(data[0]['values'])):
    x[0].append(data[0]['values'][i]['period']) # Årtal
    y[0].append(data[0]['values'][i]['values'][0]['value']) # Värde

# Följande rad ska du inte ändra på. Men du kommer att behöva ändra inne i funktionen
plot_data_multiple(x, y, cities, keys[kpi[0]]) # Detta ska plotta alla grafer
