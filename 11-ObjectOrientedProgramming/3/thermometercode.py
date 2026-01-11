import random
class Thermometer:
    def __init__(self):
        self.thermo_is_on = False
    def thermometer_is_on(self):
        self.thermo_is_on = True
        print("Thermometer is on.")
    def thermometer_is_off(self):
        self.thermo_is_on = False
        print("Thermometer is off.")
    def measure_temperature(self):
        if self.thermo_is_on:
            temperature = random.randint(340, 421)
            temperature = temperature / 10
            if temperature > 41:
                print(f"Temperature: {temperature}C (CRITICAL TEMPERATURE!!)")
            elif temperature > 37:
                print(f"Temperature: {temperature}C (fever)")
            else:
                print(f"The current temperature is {temperature}°C.")
        else:
            print("Please turn on the thermometer to measure temperature.")