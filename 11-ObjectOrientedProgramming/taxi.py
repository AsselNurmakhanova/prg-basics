class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_receipt(self):
        print(self.distance, self.fare, self.rate_per_km)



def main():
    car1 = TaxiRide(6)
    car2 = TaxiRide(7)
    car1.calculate_fare(120)
    car1.print_receipt()
    car2.calculate_fare(320)
    car2.print_receipt()

if __name__ == "__main__":
    main()
