import json
with open('reservations.json', 'r') as file:
    data = json.load(file)
    reservations = data["reservations"]
rooms = 0
paid_res = 0
unpaid_res = 0
total_value_of_paid_res = 0
total_value_of_unpaid_res = 0
for reservation in reservations:
    rooms = len(reservations)
print(f'The number of reserved rooms is: {rooms}')
for reservation in reservations:
    if reservation["paid"] == True:
        paid_res += 1
        total_value_of_paid_res += reservation["price_per_night"] * reservation["nights"]
    else:
        unpaid_res += 1
        total_value_of_unpaid_res += reservation["price_per_night"] * reservation["nights"]
print(f'The number of paid reservations is: {paid_res}')
print(f'The number of unpaid reservations is: {unpaid_res}')
print(f'The total value of paid reservations is: ${total_value_of_paid_res}')
print(f'The total value of unpaid reservations is: ${total_value_of_unpaid_res}')
