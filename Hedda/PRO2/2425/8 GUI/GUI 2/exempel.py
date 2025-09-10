import tkinter as tk
def funk():
    tal = fält.get()
    label['text'] = 'Du skrev ' + tal + ' i rutan'
root = tk.Tk()
fält = tk.Entry(root)
label = tk.Label(root)
knapp = tk.Button(root, text='Tryck här', command=funk)
fält.grid(row=1,column=1)
label.grid(row=0, column=1)
knapp.grid(row=1, column=2)
