"""
1. Läs in datan från filen ''filhantering2.csv''
2. Filen innehåller elevers resultat på ett prov.
    Betygsgränserna för godkända betyg var:
    50 (Acceptable), 70 (Exceed Expectations)
    och 90 (Outstanding).
    Skriv ut alla med godkända betyg och vad de fick.
3. Alla under 50 har fått underkänt. Där gick
    gränserna på allt under 20 (Troll), 40 (Dreadful),
    50 (Poor). Skriv ut vilka som fick vilka underkända betyg.
4. Få ditt program att skriva ut den som hade högst poäng.
5. Beräkna medelvärdet av deras resultat.
6. Vad är medianen?
7. Skriv ut hur många som fick varje betyg.
"""

with open("filhantering 2.csv") as f:
    data = f.readlines()

grades = {90: "Outstanding", 70: "Exceed expectations",
          50: "Acceptable", 40: "Poor",
          20: "Dreadful", 0: "Troll"}

godkända = []
underkända = []
for i in range(len(data)):
    data[i] = data[i].split(';')
    data[i][2] = data[i][2].strip()
    for grade in grades:
        if int(data[i][2]) >= grade:
            data[i].append(grades[grade])
            break
    
##    if int(data[i][2]) < 20:
##        data[i].append("Troll")
##        underkända.append(data[i])
##    elif int(data[i][2]) < 40:
##        data[i].append("Dreadful")
##        underkända.append(data[i])
##    elif int(data[i][2]) < 50:
##        data[i].append("Poor")
##        underkända.append(data[i])
##    elif int(data[i][2]) < 70:
##        data[i].append("Acceptable")
##        godkända.append(data[i])
##    elif int(data[i][2]) < 90:
##        data[i].append("Exceed expectations")
##        godkända.append(data[i])
##    else:
##        data[i].append("Outstanding")
##        godkända.append(data[i])
print("Godkända")
for row in godkända:
    print(" ".join(row))
print("Underkända")
for row in underkända:
    print(" ".join(row))
        
##for row in data:
##    print(row)
