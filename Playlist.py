
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
