class Song:
   def __init__(self, artist, track_title, album, year):
      self.artist = artist
      self.track_title = track_title
      self.album = album
      self.year = year
   def __str__(self):
      return f"Perfomer: {self.artist}\nTitle: {self.track_title}\nAlbum: {self.album}\nYear: {self.year}"

# object creation
song1 = Song('Ed Sheeran', 'bbbv', 'dddd', 1753)
song2 = Song('Lady Gaga', 'dfss', 'sdgsgg', 2356)

## object usage
print(song1)
print(song2)