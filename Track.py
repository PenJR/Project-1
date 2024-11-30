class Track:
    def __init__(self, title, artist, album, duration, additional_artist=None):
        """
        Initializes a new Track object.

        :param title: The title of the track
        :param artist: The main artist of the track
        :param album: The album the track belongs to
        :param duration: The duration of the track in "mm:ss" format
        :param additional_artist: Optional; Additional artists featured on the track (can be a string or list)
        """
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.additional_artist = (
            [additional_artist] if isinstance(additional_artist, str) else additional_artist or []
        )

    def get_duration_seconds(self):
        """Returns the duration of the track in seconds."""
        try:
            mins, secs = map(int, self.duration.split(':'))
            return mins * 60 + secs
        except ValueError:
            raise ValueError(f"Invalid duration format: '{self.duration}'. Expected 'mm:ss'.")

    def sort_key(self):
        """Sorting key for tracks by title, artist, album, and duration."""
        return self.title.lower(), self.artist.lower(), self.album.lower(), self.get_duration_seconds()

    def __str__(self):
        """String representation of the track."""
        additional = ", ".join(self.additional_artist) if self.additional_artist else "None"
        return (f"Title: {self.title}, Artist: {self.artist}, Album: {self.album}, "
                f"Duration: {self.duration}, Additional Artists: {additional}")

    def __eq__(self, other):
        """Equality comparison based on title, artist, album, and duration."""
        if not isinstance(other, Track):
            return False
        return self.sort_key() == other.sort_key()

    def __hash__(self):
        """Hashing method to allow using Track objects in sets and dictionaries."""
        return hash(self.sort_key())

