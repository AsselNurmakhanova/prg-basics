class TV:
   def __init__(self):
      self.is_on = False
      self.channel_no = 1
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True
   def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
   def set_channels(self, channels_list):
        self.channels_list = channels_list
   def show_channels(self):
       for index, channel in enumerate(self.channels_list, start=1):
           print(f"{index}. {channel}")
   def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no} ({self.channels_list[self.channel_no - 1]})")
        else:
            print("TV is off")