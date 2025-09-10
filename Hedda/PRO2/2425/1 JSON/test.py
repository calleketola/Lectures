import json

## Del 1

with open("data1.json") as f:
    data = json.load(f)

# Uppgift 2

print()
print("Uppgift 2:")

for x in data:
    print(x) # Skriver ut nycklarna
for x in data.values():
    if type(x) != dict:
        print(x) # Skriver ut värdet, om det inte är en dict
    else:
        for y in x:
            print(y) # Skriver ut värden i en dict

# Uppgift 3

with open("data2.json") as f:
    data2 = json.load(f)

# Uppgift 4

print()
print("Uppgift 4")
antal = len(data2)
print(f"Det finns {antal} objekt i filen")

# Uppgift 5

print()
print("Uppgift 5")
lund = 0
for x in data2:
    if data2[x]["work"]["city"] == "Lund":
        lund += 1
print(f"Det är {lund} personer som jobbar i Lund.")

# Uppgift 6
with open("data3.json") as f:
    data3 = json.load(f)

# Uppgift 7
print()
print("Uppgift 7")
antal = len(data3)
print(f"Användaren har lagt upp {antal} videoklipp.")

# Uppgift 8
print()
print("Uppgift 8")
longest = ["1", data3["1"]["length"]]
for video in data3:
    if data3[video]["length"] > longest[1]:
        longest = [video, data3[video]["length"]]
print(f"The video {data3[longest[0]]['name']} is the longest with {longest[1]} seconds.")
hours = longest[1]//60**2
minutes = (longest[1]%60**2)//60
seconds = ((longest[1]%60**2)%60)
print(f"That is {hours} hours, {minutes} minutes and {seconds} seconds!")

# Uppgift 9
print()
print("Uppgift 9")
for video in data3:
    if data3[video]["views"] < data3[video]["likes"]+data3[video]["dislikes"]:
        print(data3[video]["name"], "has more likes and dislikes than views")

# Uppgift 10
print()
print("Uppgift 10")
for video in data3:
    seconds = data3[video]["length"]
    hours = seconds//60**2
    seconds -= hours*60**2
    minutes = seconds//60
    seconds -= minutes*60
    if hours < 10:
        hours = "0"+str(hours)
    if minutes < 10:
        minutes = "0"+str(minutes)
    if seconds < 10:
        seconds = "0"+str(seconds)
    print(f"{hours}:{minutes}:{seconds} - {data3[video]['name']}")
    print(f"Views: {data3[video]['views']}")
    print(f"Likes: {data3[video]['likes']}")
    print(f"Dislikes: {data3[video]['dislikes']}")
    print()
