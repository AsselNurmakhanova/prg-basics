# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   count = 0
   for row in seats:
      for char in row:
         count += 1
   return count

def seats_available(seats):
   count = 0
   for row in seats:
      for char in row:
        if char == 'A':
            count += 1
   return count

def seats_booked(seats):
   count = 0
   for row in seats:
      for char in row:
        if char == 'B':
            count += 1
   return count

def seat_status(seats, row, place):
   seat = cinema_seats[row - 1][place - 1]
   if seats == 'A' and seat == 'A':
      return True
   else:
      return False


print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status('A', 1, 1))
print('Seat in row 5, place 5:', seat_status('A', 5, 5))
print('Seat in row 3, place 5:', seat_status('A', 3, 5))