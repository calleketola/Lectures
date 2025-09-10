from matplotlib import pyplot as plt
import requests


def approximate_line(x,y):
    """
    This is the least square method
    """
    assert len(x) == len(y)

    tot_x = 0
    tot_y = 0
    errors = []
    for i in range(len(x)):
        try:
            tot_y += y[i]
            tot_x += x[i]
        except:
            errors.append(i)
    #mean_x = sum(x)/len(x)
    #mean_y = sum(y)/len(y)
    mean_x = tot_x/(len(x)-len(errors))
    mean_y = tot_y/(len(x)-len(errors))

    m = 0

    numerator = 0
    denominator = 0

    # Calculate errors
    for i in range(len(x)):
        if i not in errors:
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
    colours = 'bgrcmyk'
    
    for i in range(len(x)): # Så att vi går igenom all data
        f = approximate_line(x[i],y[i])

        lx = [i for i in range(min(x[i]),max(x[i])+1)]
        ly = [f(a) for a in lx]
        
        plt.plot(x[i],y[i],'+'+colours[i], label=c_names[cities[i]]) # The original data
        plt.plot(lx,ly, colours[i], label=c_names[cities[i]]) # Fitted line

    plt.title(title)
    plt.legend()
    plt.show()

#data_x = [8,2,11,6,5,4,12,9,6,1]
#data_y = [3,10,3,6,8,12,1,4,9,14]
#plot_data(data_x,data_y)

# keys = ['N45900','N45905','N45912','N45920']
# nycklarnas betydelse:
# 'N45900': "Elpris inkl. moms för typfastighet enligt Nils Holgersson-modellen, kr/kvm"
# 'N45905': "Slutanvändning av energi totalt inom det geografiska området, MWh/inv"
# 'N45912': "Slutanvändning energi inom offentlig verksamhet inom det geografiska området, MWh/inv"
# 'N45920': "Slutanvändning energi inom hushåll inom det geografiska området, MWh/inv"
keys = {'N45900': "Elpris inkl. moms",
        'N45905': "Slutanvändning av energi totalt",
        'N45912': "Slutanvändning energi inom offentlig verksamhet",
        'N45920': "Slutanvändning energi inom hushåll"}

cities = [i for i in range(1280,1286)]
c_names = {1280: "Malmö",
           1281: "Lund",
           1282: "Landskrona",
           1283: "Helsingborg",
           1284: "Höganäs",
           1285: "Eslöv"}
kpi = ['N45900','N45905','N45912','N45920']
data = [[] for _ in range(len(kpi))]

# Hämta data om alla städer
for j in range(len(kpi)):
    for i in range(len(cities)):
        request = requests.get('https://api.kolada.se/v2/data/municipality/{}/kpi/{}'.format(cities[i], kpi[j]))
        data[j].append(request.json())

x = [[[] for i in range(len(cities))] for j in range(len(kpi))]
y = [[[] for i in range(len(cities))] for j in range(len(kpi))]

# Append all the values
# Will plot one graph for each key. Every graph will contain data from each city
for k in range(len(kpi)): # For every key
    for j in range(len(cities)): # For every city
        for i in range(len(data[k][j]['values'])):
            x[k][j].append(data[k][j]['values'][i]['period'])
            y[k][j].append(data[k][j]['values'][i]['values'][0]['value'])
    plot_data_multiple(x[k], y[k], cities, keys[kpi[k]])
