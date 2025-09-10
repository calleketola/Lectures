import tkinter as tk

def register_stringvar():
    widgets[5]["text"] = first_name.get() + " " + last_name.get() + " har registrerats"

def register():
    f_name = widgets[2].get()
    l_name = widgets[3].get()
    widgets[5]["text"] = f_name + " " + l_name + " har registrerats"
    
root = tk.Tk()

# När man har många widgets så gillar jag att ha dem i en lista
# det kräver dock att man dokumenterar vad som ligger vart
widgets = []

# De här två är en snajdigare lösning till register_stringvar
first_name = tk.StringVar(root, "")
last_name = tk.StringVar(root, "")

# Först de två labels som ligger överst
widgets.append(tk.Label(root, text="Förnamn"))
widgets.append(tk.Label(root, text="Efternamn"))
# De två fälten som ska ta emot data. textvariable är för den snajdiga lösningen
widgets.append(tk.Entry(root, textvariable=first_name))
widgets.append(tk.Entry(root, textvariable=last_name))
# Vår knapp vi ska trycka på
widgets.append(tk.Button(root, text="Registrera", command=register))
# Vår utskriftslabel
widgets.append(tk.Label(root))

# När man har alla i en lista kan man skriva ut dem med en for-loop
# här blir det plötsligt smidigt att använda %
for i in range(len(widgets)-2):
    widgets[i].grid(row=i//2, column=i%2)

# De två sista labelsen ska ligga annorlunda
widgets[-2].grid(row=2, column=0, columnspan=2)
widgets[-1].grid(row=3, column=0, columnspan=2)

# Det här håller programmet vid liv
root.mainloop()
