
from Track import Track

class Playlist:
    def __init__(self, name):
        self.name = name
        self.tracks = []  
        self.track_map = {}  
        self.total_duration = [0, 0]  

    def add_track(self, track: Track):
        """Add a unique track to the playlist."""
        if track.getTitle() not in self.track_map:
            self.tracks.append(track)
            self.track_map[track.getTitle()] = track 
            self._update_duration(track.getNumericDuration())
            return True
        return False

    def remove_track(self, track: Track):
        """Remove a track from the playlist."""
        track_title = track.getTitle()
        if track_title in self.track_map:
            self.tracks.remove(track) 
            self._update_duration(track.getNumericDuration(), remove=True)
            del self.track_map[track_title]  
            return True
        return False

    def _update_duration(self, duration, remove=False):
        """Update the total duration of the playlist."""
        minutes, seconds = self.total_duration
        delta_min, delta_sec = duration

        total_seconds = (minutes * 60) + seconds
        delta_seconds = (delta_min * 60) + delta_sec

        if remove:
            total_seconds -= delta_seconds
        else:
            total_seconds += delta_seconds

        self.total_duration[0] = total_seconds // 60
        self.total_duration[1] = total_seconds % 60

    def get_total_duration(self):
        """Return the total duration in 'mm:ss' format."""
        mins = self.total_duration[0]
        secs = self.total_duration[1]
        return f"{mins:02}:{secs:02}"


    def save_playlist(self):
        """Save the playlist to a file."""
        try:
           
            try:
                with open("Playlist.txt", "r") as f:
                    lines = f.readlines()
            except FileNotFoundError:
                lines = []

           
            data = {}
            for line in lines:
                key, value = line.strip().split(":", 1)
                data[key] = eval(value.strip())

            data[self.name] = {
                "Playlist Name": self.name,
                "Total Duration": self.total_duration,
                "Tracks": [track.to_dict() for track in self.tracks]
            }

           
            with open("Playlist.txt", "w") as f:
                for key, value in data.items():
                    f.write(f"{key}: {value}\n")

            print(f"Playlist '{self.name}' saved successfully.")

        except Exception as e:
            print(f"Error saving playlist: {e}")

    @staticmethod
    def load_playlist(name: str):
        """Load a playlist by name from a file."""
        try:
           
            with open("Playlist.txt", "r") as f:
                lines = f.readlines()

            data = {}
            for line in lines:
                key, value = line.strip().split(":", 1)
                data[key] = eval(value.strip())

            if name in data:
                playlist_data = data[name]
                playlist = Playlist(playlist_data["Playlist Name"])
                playlist.total_duration = playlist_data["Total Duration"]
                playlist.tracks = [Track.from_dict(track) for track in playlist_data["Tracks"]]
                return playlist
            else:
                print(f"Playlist '{name}' not found.")
                return None

        except FileNotFoundError:
            print("No saved playlists found.")
            return None
        except Exception as e:
            print(f"Error loading playlist: {e}")
            return None

    def __str__(self):
        """Return a string representation of the playlist."""
        track_list = "\n".join([str(track) for track in self.tracks])
        duration = f"{self.total_duration['minutes']} min {self.total_duration['seconds']} sec"
        return f"Playlist: {self.name}\nTotal Duration: {duration}\nTracks:\n{track_list}"

