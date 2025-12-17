import json
with open('dogs.json', 'r') as file:
    dogs = json.load(file)
for dog in dogs:
    if dog["age"] < 5:
        print(dog)