# Detta är driver koden

import random

kö = Queue() # Skapa en tom kö
for i in range(5): 
    kö.put(random.randint(1,9)) # Lägger till ett slumpat tal
    print(kö)
for i in range(5):
    kö.get() # Plockar bort ett tal
    print(kö)
