class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        """Adds a track to the library, ensuring no duplicates."""
        if any(existing_track.title.lower() == track.title.lower() and existing_track.artist.lower() == track.artist.lower() for existing_track in self.tracks):
            print(f"Track '{track.title}' by '{track.artist}' is already in the library.")
        else:
            self.tracks.append(track)
            self.sort_tracks()  # Sort tracks explicitly
            print(f"Track '{track.title}' by {track.artist} added to the library.")

    def get_tracks(self):
        """Returns the list of tracks."""
        return self.tracks

    def display_tracks(self):
        """Displays all tracks in the library."""
        if not self.tracks:
            print("No tracks in the library.")
        else:
            print("Music Library:")
            for i, track in enumerate(self.tracks, 1):
                print(f"[{i}] {track.title} – {track.artist} ({track.album}, {track.duration})")

    def search_track(self, title):
        """Search for a track by title."""
        matches = [track for track in self.tracks if title.lower() in track.title.lower()]
        if not matches:
            print(f"No tracks found with title containing '{title}'.")
        else:
            print(f"Tracks matching '{title}':")
            for track in matches:
                print(f"- {track.title} by {track.artist} ({track.duration})")
        return matches

    def sort_tracks(self):
        """Sort tracks in the library by title."""
        self.tracks.sort(key=self.get_sort_key)

    def get_sort_key(self, track):
        """Sort key function for tracks."""
        return track.title.lower()  # Sorting by track title (case-insensitive)
