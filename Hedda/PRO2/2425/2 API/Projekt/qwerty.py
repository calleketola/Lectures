import requests as r

d = r.get("https://api.kolada.se/v2/kpi_groups")

o = d.json()

kpis = {}

for j in range(len(o['values'])):
    for i in range(len(o['values'][j]['members'])):
        kpis[o['values'][j]['members'][i]["member_title"].lower()] = o['values'][j]['members'][i]["member_id"]

with open("kpis.txt", "w") as f:
    for key, value in kpis.items():
        f.write(key + ";"+value+"\n")
