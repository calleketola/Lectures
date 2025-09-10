import tkinter

def funk():
    t = textfält.get()
    text['text'] = t
    if text['bg'] != 'yellow':
        text['bg'] = 'yellow'
    else:
        text['bg'] = 'white'
    

root = tkinter.Tk()

text = tkinter.Label(root,
                     text="Kolla på mig")
text.pack()

knapp = tkinter.Button(root,
                       text="Klicka",
                       command=funk)
knapp.pack()

textfält = tkinter.Entry(root)
textfält.pack()

root.mainloop()
