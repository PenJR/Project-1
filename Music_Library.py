from Track import Track

class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        """Adds a track to the library, ensuring no duplicates."""
        if not self.duplicate(track):
            self.tracks.append(track)
            self.sort_tracks()
            print(f"Track '{track.title}' by {track.artist} added to the library.")
        else:
            print(f"Track '{track.title}' by {track.artist} already exists in the library.")

    def duplicate(self, new_track):
        """Checks if the track already exists in the library."""
        for track in self.tracks:
            if (track.title.lower() == new_track.title.lower() and
                track.album.lower() == new_track.album.lower() and
                track.artist.lower() == new_track.artist.lower()):
                return True
        return False

    def sort_tracks(self):
        """Sort tracks in the library by artist, album, and title."""
        def track_sort_key(track):
            return (track.artist.lower(), track.album.lower(), track.title.lower())

        self.tracks.sort(key=track_sort_key)

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

    def remove_track(self, title):
        """Remove a track from the library by its title."""
        for track in self.tracks:
            if track.title.lower() == title.lower():
                self.tracks.remove(track)
                print(f"Track '{track.title}' by {track.artist} removed from the library.")
                return
        print(f"No track with the title '{title}' found in the library.")

    def total_duration(self):
        """Calculate and return the total duration of all tracks in the library."""
        total_seconds = sum(track.duration_seconds() for track in self.tracks)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours} hr {minutes} min {seconds} sec"
