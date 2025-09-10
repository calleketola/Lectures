# Data maker
import json
import random
import math

N = 100

##data = [None for _ in range(N)]
##
##keys = ["temperature", "humidity", "day", "perspiration"]
##
##for i in range(N):
##    data[i] = {"search-term": random.choice(keys),
##               "values":{
##                   "temperature": f(random.random()*math.pi*2),
##                   "humidity": round(abs(math.sin(random.random())),2),
##                   "day": i,
##                   "perspiration": None
##                   }
##            
##                }
##    if data[i]["values"]["humidity"] >= 0.8:
##        data[i]["values"]["perspiration"] = round(random.random()*10,2)
##    else:
##        data[i]["values"]["perspiration"] = 0
##
##with open("data.json", "w") as f:
##    f.write(json.dumps(data, indent=4))

N = 256

data = [None for _ in range(N)]

for i in range(N):
    n = random.randint(1,10)
    data[i] = {"id": i,
               "values": {
                   "length": n,
                   "values": [random.randint(0,99) for _ in range(n)]
                   }
               }

with open("data-2.json", "w") as f:
    f.write(json.dumps(data, indent=4))
