class playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
      self.songs.remove(song)

    def view_songs(self):
        return self.songs
    def empty_playlist(self):
        self.songs.clear()
my_playlist = playlist("My Favorite Songs")
my_playlist.add_song("my heart will go on")
my_playlist.add_song("I will always love you")
my_playlist.add_song("Shape of you")
my_playlist.add_song("Perfect")

print(my_playlist.view_songs())

print(len(my_playlist.view_songs()))

my_playlist.remove_song("Shape of you")
print(my_playlist.view_songs())

my_playlist.empty_playlist()
print(my_playlist.view_songs())
