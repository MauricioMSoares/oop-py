class Song:
    songs = []

    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration
        Song.songs.append(self)

    def __str__(self):
        return f'{self.name} | {self.artist} | {self.duration}'
    
    def list_songs():
        for song in Song.songs:
            print(f'{song.name} | {song.artist} | {song.duration}')

