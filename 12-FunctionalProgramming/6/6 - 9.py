temperature = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
filter = list(filter(lambda x: temperature[x] > 0, temperature))
print(filter)