peed_limit = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed >= peed_limit:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: speed limit exceeded!!')
else:
    print("All good")