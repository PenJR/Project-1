from Track import Track

class MusicLibrary:
    def __init__(self):
        self.tracks = []
    
    def check_track(self, track):
        if self.duplicate(track):
            return "Track already exist."
        else:
            self.tracks.append(track)
            self.tracks.sort(key=Track.sort)

    def duplicate(self, new_track):
        for track in self.tracks:
            if (track.title == new_track.title and
                track.album == new_track.album and
                track.artist == new_track.artist):
                return True
        return False
     
    def display_tracks(self):
        if not self.tracks:
            return('No tracks in the library.')
        else:
            for i, track in len(self.tracks):
                return(f"[{i + 1}] {track}")
    
    def search_track(self, title):
        if not title:
            return []
        matches = [track for track in self.tracks if title.lower() in track.title.lower()]
        if not matches:
            print("No matching tracks found.")
        return matches

    def validate_duration(self, duration):
        try:
            parts = duration.split(':')
            if len(parts) != 2:
                return False
            mins = int(parts[0])
            seconds = int(parts[1])
            return mins >= 0 and 0 <= seconds < 60
        except ValueError:
            return False

    def manage_add_track(library):
        """ Handles operations related to the music library, including CRUD for Tracks.
        """
            # Add Track
        title = input("Enter track title: ")
        artist = input("Enter artist: ")
        album = input("Enter album: ")
        duration = input("Enter duration (mm:ss): ")
        additional_artist = input('Enter additional artist: ')

        try:
            track = Track(title, artist, album, duration, additional_artist)
            library.check_track(track)
            return f"Track '{title}' added successfully!"
        except ValueError as e:
            return f"Error adding track: {e}"