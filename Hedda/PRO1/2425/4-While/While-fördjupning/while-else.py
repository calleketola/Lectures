variabel = ""
försök = 0
while variabel.lower() != "chokladbollar":
    variabel = input("Bästa sortens bollar? ")
    if variabel.lower() == "fotboll":
        print("Lägg av.")
        break
    försök += 1 
else:
    print("Få saker slår chokladbollar.")
print("Du svarade", försök, "gång(er).")
