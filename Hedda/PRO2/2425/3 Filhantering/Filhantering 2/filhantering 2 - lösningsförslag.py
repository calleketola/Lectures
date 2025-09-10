"""
1. Läs in datan från filen ''filhantering2.csv''
2. Filen innehåller elevers resultat på ett prov. Betygsgränserna för godkända betyg var: 50 (Acceptable), 70 (Exceed Expectations) och 90 (Outstanding). Skriv ut alla med godkända betyg och vad de fick.
3. Alla under 50 har fått underkänt. Där gick gränserna på allt under 20 (Troll), 40 (Dreadful), 50 (Poor). Skriv ut vilka som fick vilka underkända betyg.
4. Få ditt program att skriva ut den som hade högst poäng.
5. Beräkna medelvärdet av deras resultat.
6. Vad är medianen?
7. Skriv ut hur många som fick varje betyg.
"""

with open("filhantering2.csv") as f:
    rows = f.readlines()

top_score = 0
top_scorer = ""

for row in rows:
    row = row.split(';')
    row[2] = int(row[2])
    if row[2] > top_score:
        top_score = row[2]
        top_scorer = row[0]+" "+row[1]
    if row[2] >= 90:
        row.append('Outstanding')
    elif row[2] >= 70:
        row.append("Exceed Expectations")
    elif row[2] >= 50:
        row.append("Acceptable")
    elif row[2] >= 40:
        row.append("Poor")
    elif row[2] >= 20:
        row.append("Dreadfull")
    else:
        row.append("Troll")
    for data in row:
        print(data, end=" ")
    print()
print(top_scorer)
