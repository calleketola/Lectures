import tkinter
import sqlite3

con = sqlite3.connect('Djur.db')

cur = con.cursor()

def funk():
    com = sql_command.get()
    output = ""
    for row in cur.execute(com):        
        output += str(row) +"\n"
    result["text"] = output

root = tkinter.Tk()



sql_command = tkinter.Entry(root)
sql_command.pack()

knapp = tkinter.Button(root, text="Kör", command=funk)
knapp.pack()


result = tkinter.Label(root, text="Output")
result.pack()

root.mainloop()
