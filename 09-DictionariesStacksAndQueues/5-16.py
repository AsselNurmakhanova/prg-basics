import json
with open('computer.json', 'r', encoding='utf-8') as file:
   # Load the data from the JSON file into a variable
   data = json.load(file)
for char , describtion in data.items():
   print(char,':',describtion)