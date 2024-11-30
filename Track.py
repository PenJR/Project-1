class Track:
    def __init__(self, title, artist, album, duration):
        """
        Initializes a new Track object.

        :param title: The title of the track
        :param artist: The artist of the track
        :param album: The album of the track
        :param duration: The duration of the track in "mm:ss" format
        """
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration