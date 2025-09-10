import json

#############
# ÖVNING 01 #
#############

# Läs in data1
with open("data1.json") as f:
    data1 = json.load(f)
    
#############
# ÖVNING 02 #
#############
print("Övning 02\n")


# Skriver ut alla nycklar och värden
print("Nycklar och värden")
for key in data1:
    print(key, data1[key])

print()
#############
# ÖVNING 03 #
#############

# Läser in data2
with open("data2.json") as f:
    data2 = json.load(f)

#############
# ÖVNING 04 #
#############

print("Övning 04\n")

# Skriver ut antalet objekt
print("Antal objekt:", len(data2))

#############
# ÖVNING 05 #
#############

print("\nÖvning 05\n")

lundensare = 0
# Räkna hur många som jobbar i Lund
for person in data2: # Loopar igenom alla nycklar
    if data2[person]['work']['city'].lower() == 'lund': # Varför tar jag lower?
        lundensare += 1
print("Antal som jobbar i Lund:", lundensare)

#############
# ÖVNING 06 #
#############

# Läser in data3
with open("data3.json") as f:
    data3 = json.load(f)

#############
# ÖVNING 07 #
#############

print("\nÖvning 07\n")

print("Antal videos:", len(data3))

#############
# ÖVNING 08 #
#############

print("\nÖvning 08\n")

# Hitta längsta klippet
tid = 0
längst = '1'
for video in data3:
    if data3[video]['length'] >= tid: # Om längre än den tidigare längsta
        tid = data3[video]['length']
        längst = video
print("Det längsta klippet är", data3[längst]['name'], "med tiden", tid)

#############
# ÖVNING 09 #
#############

print("\nÖvning 09\n")

# Kolla om likes + dislikes > views
print("Följande videor har fler likes och dislikes än views:")
for video in data3:
    if data3[video]['views'] < data3[video]['likes']+data3[video]['dislikes']:
        print(data3[video]['name'])

#############
# ÖVNING 10 #
#############

print("\nÖvning 10\n")

# Skriv ut i formatet hh:mm:ss - titel
for video in data3:
    time = data3[video]['length']
    # Räknar ut sekunder, minuter, timmar och strängar dem
    seconds = str(time%60)
    minutes = str((time//60)%60)
    hours = str((time//60)//60)

    # Fixa det till tvåsiffriga svar
    if len(seconds) < 2:
        seconds = "0"+seconds
    if len(minutes) < 2:
        minutes = "0"+minutes
    if len(hours) < 2:
        hours = "0"+hours
    
    print(hours+":"+minutes+":"+seconds+" - "+data3[video]['name'])
    
