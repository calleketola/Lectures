import tkinter


def check_numbers(t1, t2):
    try:
        t1 = float(t1)
        t2 = float(t2)
        return True
    except ValueError:
        return False

def fix_numbers(t1, t2):
    return float(t1), float(t2)

def print_svar(s):
    if s != "Ogiltiga tal":
        # Gör om till en sträng
        s = "="+str(s)
    # Uppdaterar svarstexten
    svar['text'] = s
    

def add():
    # Läs in talen
    tal1 = talf1.get()
    tal2 = talf2.get()

    res = ""
    # Kollar om talen är OK
    if check_numbers(tal1, tal2):
        # Fixar talen
        tal1, tal2 = fix_numbers(tal1,tal2) # : tal1 = float(tal1)
        # Gör matten
        res = tal1+tal2
    else:
        res = "Ogiltiga tal"
    # Skicka vidare svaret
    print_svar(res)
    #svar['text'] = res
    
def subtract():
    tal1 = talf1.get()
    tal2 = talf2.get()

    res = ""
    if check_numbers(tal1, tal2):
        tal1, tal2 = fix_numbers(tal1,tal2)
        res = tal1-tal2
    else:
        res = "Ogiltiga tal"

    print_svar(res)


def multiply():
    tal1 = talf1.get()
    tal2 = talf2.get()

    res = ""
    if check_numbers(tal1, tal2):
        tal1, tal2 = fix_numbers(tal1,tal2)
        res = tal1*tal2
    else:
        res = "Ogiltiga tal"

    print_svar(res)


def divide():
    tal1 = talf1.get()
    tal2 = talf2.get()

    res = ""
    if check_numbers(tal1, tal2):
        tal1, tal2 = fix_numbers(tal1,tal2)
        if tal2 != 0:
            res = tal1/tal2
        else:
            res = "Nolldivision"
    else:
        res = "Ogiltiga tal"

    print_svar(res)
    
# Skapa fönstret
root = tkinter.Tk()
la = tkinter.Label(root, text="Miniräknare 0.1")
la.pack()

# Talen
talf1 = tkinter.Entry(root)
talf2 = tkinter.Entry(root)

talf1.pack()
talf2.pack()

# Svaret
svar = tkinter.Label(root, text="= ")
svar.pack()

# Knappar
b1 = tkinter.Button(root, text="+", command=add)
b2 = tkinter.Button(root, text="-", command=subtract)
b3 = tkinter.Button(root, text="x", command=multiply)
b4 = tkinter.Button(root, text="/", command=divide) # and conquer

b1.pack()
b2.pack()
b3.pack()
b4.pack()

root.mainloop()
