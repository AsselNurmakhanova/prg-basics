seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
sorted = sorted(file_name)

# Write data to the file
    with open(file_name, 'w') as file:
      for item in file:
         ... .write(...)