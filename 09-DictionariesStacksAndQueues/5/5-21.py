import json
product = {}
product["name"] = input("Enter product name: ")
product["price"] = float(input("Enter product price: "))
product["paid"] = bool(input("Enter if paid (True/False): "))
file_name = "product.json"
with open(file_name, 'w') as file:
   json.dump(product, file, indent=4)
print("Data has been written to", file_name)