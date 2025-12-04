class Phone():
    def __init__(self, battery_level, storage, network_status):
        self.battery_level = battery_level
        self.storage = storage
        self.network_status = network_status
    def charge_battery(self):
        if self.battery_level < 15:
            print(f"Your battery level is {self.battery_level}%, it is too low, please charge it")
        else:
            print(f"Your battery level is {self.battery_level}%")

    def install_app(self, app_size):
        if self.storage - app_size < 0:
            print("Not enough space to install the app.")
        else:
            self.storage -= app_size
            print(f"App installed. Current storage used: {self.storage} GB")

    def toggle_network(self, change):
        if change == True:
            if self.network_status == "Mobile Data":
                self.network_status == "WI-FI"
            else:
                self.network_status = "Mobile Data"
        print(f"Network status is now: {self.network_status}")

    def display_phone_status(self):
        print(f"Battery level: {self.battery_level}%")
        print(f"Storage used: {self.storage} GB")
        print(f"Network status: {self.network_status}")

my = Phone(12,127,'WI-FI')
my.charge_battery()
my.install_app(128)
my.toggle_network(True)