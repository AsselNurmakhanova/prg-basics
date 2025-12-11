
def avg_speed(distance, hours, minutes):
    total_time_in_hours = hours + (minutes / 60)
    speed = distance / total_time_in_hours
    return speed

distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))
result = avg_speed(distance, hours, minutes)
print(f"Average speed: {result:.1f} km/h")
