from thermometercode import Thermometer
def main():
    thermo = Thermometer()
    thermo.thermometer_is_on()
    thermo.measure_temperature()
    thermo.thermometer_is_off()
    thermo.measure_temperature()
    
if __name__ == "__main__":
    main()