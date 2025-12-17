hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    names = []
    for h in hotels:
        names.append(h["name"])
    return names

def average_price(hotels):
    total = 0
    for h in hotels:
        total += h["price"]
    return total / len(hotels)
print("Hotels in Krakow:", *hotel_list(hotels_in_Krakow))
print("Average price in Krakow:", average_price(hotels_in_Krakow))
print("Hotels in Sopot:", *hotel_list(hotels_in_Sopot))
print("Average price in Sopot:", average_price(hotels_in_Sopot))