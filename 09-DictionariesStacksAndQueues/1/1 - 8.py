price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for item, price in price_list.items():
    print(f"Price without discount: {item}: ${price}")
sum = 0
for price in price_list.values():
    sum += price
print(f"Total price without discount: ${sum:.2f}")
for item, price in price_list.items():
    discounted_price = price * 0.9
    print(f"Price with 10% discount: {item}: ${discounted_price:.2f}")
total_discounted_sum = 0
for price in price_list.values():
    total_discounted_sum += price * 0.9
print(f"Total price with 10% discount: ${total_discounted_sum:.2f}")