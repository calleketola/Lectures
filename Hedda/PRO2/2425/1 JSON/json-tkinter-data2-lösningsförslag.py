import tkinter as tk
import json

with open("data2.json", encoding="utf-8") as f:
    data = json.load(f)

root = tk.Tk()

persons = []
i = 0 # Detta är en fuling...
for key in data:
    if i%2==0:
        color = "#eeeeee"
    else:
        color= "#dddddd"
    i += 1
    
    new_person = []

    new_person.append(tk.Label(
                                root,
                               text=(data[key]['firstName']
                                     +" "
                                     +data[key]['lastName']),
                                background=color))
    
    new_person.append(tk.Label(root, text=data[key]['work']['workspace'],background=color))
    
    new_person.append(tk.Label(root, text=data[key]['work']['city'],background=color))
    
    persons.append(new_person)
    

for i in range(len(persons)):
    for j in range(len(persons[i])):
        # Den komplicerade formeln gör att datan grupperas snyggt
        persons[i][j].grid(row=(i//3)*3+j, column=i%3,sticky="ewns")
        # Sticky gör att färgerna går ända ut i kanten

root.mainloop()
