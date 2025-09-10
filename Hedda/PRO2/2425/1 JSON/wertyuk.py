import json

with open('data1.json') as f:
    data = json.load(f)

print(data['work']['city'])
