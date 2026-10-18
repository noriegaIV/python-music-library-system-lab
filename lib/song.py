class Song:
    # Class attributes (shared by all Song objects)
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    artists_count = artist_count  # alias: same dictionary, works with either name

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Each class method is triggered when a new song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increment the total number of songs by one."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Add a genre to the genres list only if it's not already there."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Add an artist to the artists list only if it's not already there."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """Increment the genre's count, starting at 1 if it's new."""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """Increment the artist's count, starting at 1 if it's new."""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


if __name__ == "__main__":
    Song("99 Problems", "Jay-Z", "Rap")
    Song("Halo", "Beyonce", "Pop")
    Song("Empire State of Mind", "Jay-Z", "Rap")

    print(Song.count)         # 3
    print(Song.genres)        # ['Rap', 'Pop']
    print(Song.artists)       # ['Jay-Z', 'Beyonce']
    print(Song.genre_count)   # {'Rap': 2, 'Pop': 1}
    print(Song.artist_count)  # {'Jay-Z': 2, 'Beyonce': 1}